import pandas as pd


def to_pep8(name: str):
    return name.lower().replace(' ', '_')


df = pd.read_csv('data.csv', sep=',', encoding='cp1251')
df.rename(columns={x: to_pep8(x) for x in df.columns}, inplace=True)

new_df = df.loc[(df['номер_конвейера'] == 1) & (df['номер_смены'] == 2)][['вес', 'брак']].sort_values(by='вес')
new_df['брак'] = new_df['брак'].apply(lambda x: 1 if x == 'Годен' else 0)

corr = new_df.corr('pearson')
result = abs(round(corr['брак']['вес'], 4))
print(result)