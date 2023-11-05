import pandas as pd
from scipy.stats import ttest_ind, mannwhitneyu, shapiro


data = pd.read_csv('задача_2.csv', sep=';', decimal=',', encoding='cp1251')

df1 = data[data['group'] == 'group_1']
df2 = data[data['group'] == 'group_2']

cat = data.columns.to_list()[1:]


def check_normality(group):
    return shapiro([group[i] for i in cat]).pvalue


def choose_method(normality, category):
    if normality <= 0.05:
        return mannwhitneyu(df1[category], df2[category]), 'Манн-Уитни'
    return ttest_ind(df1[category], df2[category]), 'Стьюдент'


results = [['показатель', 'р-уровень', 'метод расчёта']]

for i in cat:
    result, method = choose_method(check_normality(df1), i)
    p_value = round(result.pvalue, 4)
    results.append([i, p_value, method])

results = [results[0]] + sorted(results[1:], key=lambda x: x[1])

print(results)