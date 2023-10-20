import pandas as pd
from scipy.stats import chi2_contingency
from numpy import sqrt


def to_pep8(name: str):
    return name.lower().replace(' ', '_')


def cramers_v(x, y):
    confusion_matrix = pd.crosstab(x, y)
    chi2 = chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum().sum()
    phi2 = chi2 / n
    r, k = confusion_matrix.shape
    return sqrt(phi2 / min((k - 1), (r - 1)))


df = pd.read_csv('data.csv', sep=',')
df.rename(columns={x: to_pep8(x) for x in df.columns}, inplace=True)

new_df = df.loc[(df['ингредиент_1'] < 270) & (df['номер_смены'] == 2)][['оператор_линии', 'брак']]
new_df['брак'] = new_df['брак'].apply(lambda x: 1 if x == 'Годен' else 0)

print(round(cramers_v(new_df['оператор_линии'], new_df['брак']), 4))
