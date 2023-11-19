import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

df = pd.read_csv('data.csv', delimiter=';', decimal=',')

df['температура'] = df['температура']
df['дождь'] = df['дождь'].astype('category')
df['продажи'] = df['продажи']

X = df[['температура', 'дождь']]
y = df['продажи']

column_transformer = ColumnTransformer(
    transformers=[
        ('onehot', OneHotEncoder(), ['дождь'])
    ], 
    remainder='passthrough'
)

X_transformed = column_transformer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.15, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

print(np.round(model.predict(X_test)))