import pandas as pd


df = pd.read_csv('data56.csv', delimiter=',')
df = df[['расстояние_кат', 'путешествует_с_детьми', 'общая_оценка_качества_предоставленной_услуги']]
df = df[df['общая_оценка_качества_предоставленной_услуги'] == 'плохо']
df = df.groupby(['расстояние_кат'])
df = round(df[['расстояние_кат', 'путешествует_с_детьми']].value_counts(normalize=True).apply(lambda x: x * 100), 1)
s = str(df.to_frame().sort_index())
print(0, s.lstrip()[11:], sep='\n')