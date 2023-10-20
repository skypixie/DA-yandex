import pandas as pd


def to_pep8(name: str):
    return name.lower().replace(' ', '_')


df = pd.read_csv('data.csv', sep=',', encoding='cp1251')
df.rename(columns={x: to_pep8(x) for x in df.columns}, inplace=True)

new_df = df[['вес', 'ингредиент_1', 'ингредиент_2']]
print(new_df.corr())