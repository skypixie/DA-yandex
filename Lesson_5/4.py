import pandas as pd
from scipy.stats import pearsonr, spearmanr, shapiro

df = pd.read_csv('задача_4.csv', sep=';', decimal=',', encoding='cp1251')

factors = df.columns[1:]

result_list = []

for i in range(len(factors)):
    factor1 = factors[i]
    for j in range(len(factors)):
        if i == j:
            continue
        factor2 = factors[j]

        group_a = df.loc[df['Группа'] == 'Группа_1', factor1]
        group_b = df.loc[df['Группа'] == 'Группа_1', factor2]

        normal_dist_factor1 = shapiro(group_a)[1] > 0.05
        normal_dist_factor2 = shapiro(group_b)[1] > 0.05

        if normal_dist_factor1 and normal_dist_factor2:
            corr_value, p_value = pearsonr(df[df['Группа'] == 'Группа_1'][factor1],
                                           df[df['Группа'] == 'Группа_1'][factor2])
            method = 'Пирсон'
        else:
            corr_value, p_value = spearmanr(df[df['Группа'] == 'Группа_1'][factor1],
                                            df[df['Группа'] == 'Группа_1'][factor2])
            method = 'Спирмен'

        corr_value = round(corr_value, 2)
        p_value = round(p_value, 4)

        if p_value >= 0.05:
            continue

        result_list.append([factor1, factor2, corr_value, p_value, method])

result_list.sort(key=lambda x: x[2], reverse=True)

print([['показатель 1', 'показатель 2', 'значение корреляции',
        'р-уровень', 'метод корреляции']] + result_list)