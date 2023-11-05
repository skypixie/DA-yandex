import pandas as pd
from scipy.stats import chi2_contingency


data = pd.read_csv('задача_3.csv', sep=';', decimal=',', encoding='cp1251')
complications = data.columns.to_list()[2:]

header = [['показатель', 'р-уровень']]
result = []

for i in complications:
    confusion_matrix = pd.crosstab(data[i], data['вид_зондирования'])
    
    _, p, _, _ = chi2_contingency(confusion_matrix)
    
    result.append([i, round(p, 4)])

result.sort(key=lambda x: x[1])

result = header + result

print(result)