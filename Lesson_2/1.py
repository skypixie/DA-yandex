import pandas as pd


def to_pep8(name: str):
    return name.lower().replace(' ', '_')


df = pd.read_csv('data.csv', sep=',', encoding='cp1251')
df.rename(columns={x: to_pep8(x) for x in df.columns}, inplace=True)
df = df[['покупательская_активность',
         'тип_сервиса',
         'разрешить_сообщать',
         'популярная_категория']]
print(df.describe().T)