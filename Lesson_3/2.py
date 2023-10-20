import pandas as pd
from numpy import NaN


def to_pep8(name: str):
    return name.lower().replace(' ', '_')


df = pd.read_csv('data_2.csv', sep=',', encoding='cp1251')
df.rename(columns={x: to_pep8(x) for x in df.columns}, inplace=True)

sum_df = df.groupby(['key']).sum()
corr = sum_df.corr(method='spearman')

for cat in ['полная_мощность', 'время_нагрева', 'вес_добавки']:
    corr.loc[abs(corr[cat]) < 0.85, cat] = NaN

print(corr)