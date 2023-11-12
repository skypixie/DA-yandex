import pandas as pd


df = pd.read_csv('tag_3.csv', delimiter=';', decimal=',', encoding='cp1251')
df.rename(columns={'Вес': 'вес',
                       'Затрачиваемая мощность': 'затрачиваемая_мощность'},
              inplace=True)

df['затрачиваемая_мощность'].interpolate(method='linear', limit=1, inplace=True)
df['затрачиваемая_мощность'].fillna(df.groupby('key')['затрачиваемая_мощность'].transform('median'), inplace=True)

df['вес'].ffill(inplace=True)

new_df = df.groupby('key').agg({'вес': 'sum', 'затрачиваемая_мощность': 'sum'}).reset_index()

new_df = new_df.round()

print(new_df[['вес', 'затрачиваемая_мощность']].head(30))
