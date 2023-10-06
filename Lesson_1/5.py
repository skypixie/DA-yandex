import pandas as pd


df = pd.read_csv('data56.csv', sep=',')
df = df[['путешествует_с_детьми', 'общая_оценка_качества_предоставленной_услуги']]
df = df.groupby(['путешествует_с_детьми']).value_counts(normalize=True).apply(lambda x: round(x * 100, 1)).to_frame()
s = str(df.sort_index())
print(0, s.lstrip()[11:], sep='\n')