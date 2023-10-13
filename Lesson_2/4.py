import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def to_pep8(name: str):
    return name.lower().replace(' ', '_').strip()


df = pd.read_csv('data.csv', sep=',', encoding='cp1251')
df.rename(columns={x: to_pep8(x) for x in df.columns}, inplace=True)
column = to_pep8(input())

customer_activity_cat_lst = df['покупательская_активность'].unique()
ca_dfs = [
    df[df['покупательская_активность'] == customer_activity_cat_lst[i]] for i \
        in range(len(customer_activity_cat_lst))
]

for cat in ca_dfs:
    sns.kdeplot(cat, fill=True)

'''sns.kdeplot(df[column].to_frame(), x=column, fill=True, legend=True)
plt.ylabel('')
plt.show()'''