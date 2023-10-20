import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def to_pep8(name: str):
    return name.lower().replace(' ', '_')


df = pd.read_csv('data.csv', sep=',', encoding='cp1251')
df.rename(columns={x: to_pep8(x) for x in df.columns}, inplace=True)
y = input()

fig, ax = plt.subplots()

fig = sns.scatterplot(data=df,
                      x='вес',
                      y=y,
                      hue='оператор_линии')
plt.suptitle(t='Диаграмма рассеяния:\nАнализ зависимости между факторами', y=1.01, fontsize=16)
fig = ax.get_figure()
fig.savefig('target_3_7.png')
