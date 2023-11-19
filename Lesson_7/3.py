import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import r2_score, mean_absolute_error

df = pd.read_csv('data.csv', delimiter=';', decimal=',')

df['кузов'] = df['кузов'].apply(lambda x: 0 if x == 'седан' else 1)
df[['цена', 'возраст', 'мощность']] = df[['цена', 'возраст', 'мощность']].apply(pd.to_numeric)

X = df[['возраст', 'мощность', 'кузов']]
y = df['цена']

column_transformer = ColumnTransformer(
    [('onehot', OneHotEncoder(), ['кузов'])],
    remainder='passthrough'
)

X_transformed = column_transformer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.15, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"{r2:.2f} {mae:.2f}")