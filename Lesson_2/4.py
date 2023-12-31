import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def to_pep8(name: str):
    return name.lower().replace(' ', '_').strip()


# read and prepare csv
df = pd.read_csv('data.csv', sep=',')
df.rename(columns={x: to_pep8(x) for x in df.columns}, inplace=True)
column = to_pep8(input())

fig, ax = plt.subplots()

fig = sns.kdeplot(data=df,
                  x=column,
                  hue='покупательская_активность',
                  fill=True,
                  legend=True)

plt.ylabel(None)
fig = ax.get_figure()
fig.savefig('target_2_4.png')
