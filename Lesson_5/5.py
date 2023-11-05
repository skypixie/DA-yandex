import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('задачи_1_и_5.csv', sep=';', encoding='cp1251')
x = input()
a = df[(df['регион'] == x)]['время_до']
b = df[(df['регион'] == x)]['время_после']

newdf = []
for q in a:
    newdf.append([q, 'время_до'])
for q in b:
    newdf.append([q, 'время_после'])

s = pd.DataFrame(newdf)
s.columns = ['num', 'class']
ax = sns.boxplot(data=s, x="num", y="class")
ax.set_xlabel('время')
plt.savefig('target_5_5.png')