import pandas as pd
from math import sqrt


df = pd.read_csv('data.csv', sep=';', decimal=',').dropna()
n, p, Z = df.iat[0, 0], df.iat[0, 1], df.iat[0, 2]

H = (Z * sqrt(p * (1 - p) / n))
print(round((p - H) * 100, 2), round((p + H) * 100, 2))
