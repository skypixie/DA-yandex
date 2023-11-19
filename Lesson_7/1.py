import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np


df = pd.read_csv('data.csv', delimiter=';', decimal=',')

X = df[['температура', 'влажность']]
y = df['продажи']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print(np.round(model.predict(X_test)))