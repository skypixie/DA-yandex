import pandas as pd
from math import sqrt


df = pd.read_csv('cake_5.csv', skipinitialspace=True,
                 decimal=',', encoding='cp1251')
new_df = df[df['вес_шоколадки'] >= 100]

Z = 1.96
N = 8000
n = len(new_df)
p = n / len(df)

n_adjusted = (n * N) / (N + n - 1)

H = round((Z * sqrt(p * (1 - p) / n_adjusted)), 3)
H_5 = round(H / 5, 3)
n_new = (Z * sqrt(p * (1 - p)) / H_5) ** 2

n_final = int((7999 * n_new) / (8000 - n_new))

print(H, n_final, sep=' , ')