import pandas as pd
import numpy as np
from scipy.stats import ttest_ind, mannwhitneyu, shapiro


def to_pep8(s: str):
    return s.lower().replace(' ', '_')


# Загрузка данных
data = pd.read_csv('data.csv', sep=';', decimal=',')
data.rename(columns={x: to_pep8(x) for x in data.columns}, inplace=True)

# Очистка данных
# Заполнение пропусков медианой
data['выручка'] = data.groupby(['покупательская_активность', 'тип_товара'])['выручка']\
    .transform(lambda x: x.fillna(x.median()))

# Определение выбросов
Q1 = data['выручка'].quantile(0.25)
Q3 = data['выручка'].quantile(0.75)
IQR = Q3 - Q1
data['выручка'] = np.where(data['выручка'] > Q3 + 3 * IQR, Q3 + 3 * IQR, data['выручка'])


columns = data.columns[2:].to_list()
result = [['показатель', 'р-уровень', 'метод расчёта р-уровня']]

for cat in columns:
    # Группировка данных
    group1 = data[(data['покупательская_активность'] == 'Снизилась') & (data['тип_товара'] == 'товары для себя')][cat]
    group2 = \
        data[(data['покупательская_активность'] == 'Прежний уровень') & (data['тип_товара'] == 'товары для себя')][cat]

    # Проверка на нормальность
    _, p_value_group1 = shapiro(group1)
    _, p_value_group2 = shapiro(group2)
    # Если данные в обеих группах нормально распределены, то используем t-тест
    if p_value_group1 > 0.05 and p_value_group2 > 0.05:
        t_stat, p_value = ttest_ind(group1, group2, equal_var=False)
        method = 'Стьюдент'
    else:  # Иначе используем Манн-Уитни
        t_stat, p_value = mannwhitneyu(group1, group2)
        method = 'Манн-Уитни'
    result.append([cat, round(p_value, 4), method])

# Вывод результатов
print(result)