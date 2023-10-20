import pandas as pd
import matplotlib.pyplot as plt


def to_pep8(name: str):
    return name.lower().replace(' ', '_').strip()


# read and prepare csv
df = pd.read_csv('data.csv', sep=',')
df.rename(columns={x: to_pep8(x) for x in df.columns}, inplace=True)
column = to_pep8(input())

fig, ax = plt.subplots()
ax.pie(df[column].value_counts(),
       labels=df[column].value_counts().index.to_list(),
       autopct='%1.1f%%')

fig.savefig('target_2_5.png')