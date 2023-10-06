import pandas as pd


def to_pep8(name: str):
    return name.lower().replace(' ', '_')


df = pd.read_csv('data2.csv', sep=',')

df.rename(columns={x: to_pep8(x) for x in df.columns}, inplace=True)

df['возраст'] = df['возраст'].replace(',', '.', regex=True)

df = df.astype({'возраст': float})

df['возраст'] = df['возраст'].apply(lambda x: round(x))

print(df[['возраст', 'путешествует_с_детьми']].head(10))
