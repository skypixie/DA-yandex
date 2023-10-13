import pandas as pd


def to_pep8(name: str):
    return name.lower().replace(' ', '_')


df = pd.read_csv('data.csv', sep=',', encoding='cp1251')
df.rename(columns={x: to_pep8(x) for x in df.columns}, inplace=True)
new_df = df[['разность_выручки_тек_прошлый_месяц', 'покупательская_активность']].groupby(['покупательская_активность'])
#print('\n'.join((str(new_df.describe().astype('int').head()).split('\n')[1:])))
print('\n'.join(new_df.describe().astype('int').to_string().split('\n')[1:]))