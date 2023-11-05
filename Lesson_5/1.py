import pandas as pd
from scipy.stats import mannwhitneyu

data = pd.read_csv('задачи_1_и_5.csv', sep=';', decimal=',',
                   skipinitialspace=True, encoding='cp1251').dropna()

regions = data['регион'].unique()
regions_dataframes = [
    data[data['регион'] == r] for r in regions
]


header = [['регион', 'р-уровень']]
result = []

for df in regions_dataframes:
    region = df['регион'].unique()[0]
    p = round(mannwhitneyu(df['время_до'], df['время_после']).pvalue, 4)

    result.append([region, p])

result = header + sorted(result, key=lambda x: x[1])
print(result)
