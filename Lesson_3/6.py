import pandas as pd
from scipy.stats import chi2_contingency
from math import sqrt


def to_pep8(name: str):
    return name.lower().replace(' ', '_')


def cramers_v(x, y):
    confusion_matrix = pd.crosstab(x, y)
    chi2 = chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum().sum()
    phi2 = chi2 / n
    r, k = confusion_matrix.shape
    return sqrt(phi2 / min((k - 1), (r - 1)))


df = pd.read_csv('data.csv', sep=',', encoding='cp1251').dropna()
df.rename(columns={x: to_pep8(x) for x in df.columns}, inplace=True)
df['ингредиент_кат'] = df['ингредиент_1'].apply(lambda x: 'менее_270' if (x < 270) else 'более_270')

new_df = df[['ингредиент_кат', 'брак']]
print(round(cramers_v(new_df['ингредиент_кат'], new_df['брак']), 4))
