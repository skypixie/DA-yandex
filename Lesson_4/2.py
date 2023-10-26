import pandas as pd
from math import sqrt


milage = pd.read_csv('avto_2.csv', decimal=',', sep=';', encoding='cp1251')
milage_sample = milage[milage['пробег'] > 140]

N = 1200
n = len(milage_sample)
p = n / len(milage)
Z = 1.96

n_adjusted = (n * N) / (N + n - 1)

H = Z * sqrt(p * (1 - p) / n_adjusted)
print(round((p - H) * 100, 2), round((p + H) * 100, 2))