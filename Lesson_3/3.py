import pandas as pd


def to_pep8(name: str):
    return name.lower().replace(' ', '_')


df = pd.read_csv('data.csv', sep=',', encoding='cp1251')
df.rename(columns={x: to_pep8(x) for x in df.columns}, inplace=True)

# ингредиент_1, брак
new_df = df[['брак', 'ингредиент_1']].sort_values(by=['ингредиент_1', 'брак'])

new_df['брак'] = new_df['брак'].apply(lambda x: 1 if x == 'Годен' else 0)
corr = new_df.corr('pearson')
result = abs(round(corr['брак']['ингредиент_1'], 4))
print(result)