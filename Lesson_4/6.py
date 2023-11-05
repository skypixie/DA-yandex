import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def to_pep8(s):
    return s.replace(' ', '_').lower()


df = pd.read_csv('data.csv', sep=',')
df.rename(columns={x: to_pep8(x) for x in df.columns}, inplace=True)
inp = input()
selected_data = df[df['покупательская_активность'] == inp]\
    .reset_index(drop=True)

plt.figure(figsize=(9, 3))

# Гистограмма
ax1 = plt.subplot(1, 2, 1)
sns.histplot(data=selected_data, x='выручка_от_клиента_текущий_месяц',
             kde=True,
             bins=30, ax=ax1)
plt.title('')
plt.xlabel('')
plt.ylabel('')

# Ящик с усами
ax2 = plt.subplot(1, 2, 2)
sns.boxplot(data=selected_data, y='выручка_от_клиента_текущий_месяц', ax=ax2)
plt.title('')
plt.xlabel('')
plt.ylabel('')

# Добавляем заголовок к графикам
plt.suptitle('Гистограмма и ящик с усами для количественных данных')

# Сохранение графика
plt.savefig('target_4_6.png')