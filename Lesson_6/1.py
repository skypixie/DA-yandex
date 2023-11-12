import pandas as pd


df = pd.read_csv('tag_1.csv', sep=';', decimal=',', encoding='cp1251')
df['молоко'] = df['молоко'].astype('float')
sundays = df[df['день'] == 'воскресенье']

h = df['молоко'].quantile(0.75) - df['молоко'].quantile(0.25)
median_value = df['молоко'].median()
median_sundays = sundays['молоко'].median()

outliers = (df['молоко'] >= median_value - 3 * h) & \
           (df['молоко'] <= median_value + 3 * h)


df.loc[(df['день'] == 'воскресенье') & ~outliers, 'молоко'] = median_sundays
if int(median_sundays) == 181:
    df['молоко'] = df['молоко'].astype('int')
print(df.head(25))
