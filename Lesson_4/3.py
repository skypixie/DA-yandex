import pandas as pd


df = pd.read_csv('data.csv', sep=';',
                        decimal=',')
df = df[df['название'] == 'полёт']['вес_шоколадки']
# удалить супервыбросы
df = df.loc[(df > df.quantile(0.01)) & (df < df.quantile(0.99))]

Z = 1.96
disp = df.var()
H = 1
n = (Z * disp / H) ** 2

print(int(n))