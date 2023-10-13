import pandas as pd


def to_pep8(name: str):
    return name.lower().replace(' ', '_')


df = pd.read_csv('data.csv', sep=',')
df.rename(columns={x: to_pep8(x) for x in df.columns}, inplace=True)
column = to_pep8(input())

ax = df[column].plot.hist(grid=True)
fig = ax.get_figure()
fig.savefig('target_2_3.png')