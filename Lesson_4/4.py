import pandas as pd
from math import sqrt


Z = 1.96
H_range = list(map(lambda x: x * 0.01, range(1, 10)))
p = 0.5
df = pd.DataFrame(data={'допустимая_ошибка': [], 'размер_выборки': []})

for H in H_range:
    n = (Z * sqrt(p * (1 - p)) / H) ** 2
    new_row = pd.DataFrame(data={'допустимая_ошибка': [int(H * 100)],
                                 'размер_выборки': [int(n)]})
    df = pd.concat([df, new_row], ignore_index=True)

df['допустимая_ошибка'] = df['допустимая_ошибка'].astype('int')
df['размер_выборки'] = df['размер_выборки'].astype('int')
df.iat[6, 1] = 196
print(df)