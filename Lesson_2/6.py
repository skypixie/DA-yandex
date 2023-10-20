import pandas as pd


def to_pep8(name: str):
    return name.lower().replace(' ', '_').strip()


def decide_product_category(category):
    if category == 'Товары для детей':
        return 'покупки для детей'
    elif category in ['Домашний текстиль', 'Кухонная посуда',
                      'Мелкая бытовая техника и электроника']:
        return 'покупки для быта'
    elif category in ['Косметика и аксессуары', 'Техника для красоты и здоровья']:
        return 'покупки для себя'


# read and prepare csv
df = pd.read_csv('data.csv', sep=',')
df.rename(columns={x: to_pep8(x) for x in df.columns}, inplace=True)

df['категории_товаров'] = df['популярная_категория'].apply(lambda x: decide_product_category(x))

general_purchases = df[df['категории_товаров'] == 'покупки для быта']\
    .groupby(['покупательская_активность'])[['разность_выручки_тек_прошлый_месяц']]
print('\n'.join(general_purchases.describe().astype('int').to_string().split('\n')[1:]))