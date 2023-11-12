import pandas as pd


df = pd.read_csv('tag_2.csv', sep=';', decimal=',')


def get_most_frequent(brand, model):
    target = df[(df['Brand'] == brand) & (df['Model'] == model)]
    
    if not target.empty:
        mode_result = target['VehicleType'].mode()
        
        if not mode_result.empty:
            return mode_result.iat[0]
    
    return 'unknown'


def replace_empty_with_mode(row):
    if pd.isnull(row['VehicleType']):
        return get_most_frequent(row['Brand'], row['Model'])
    return row['VehicleType']


df['VehicleType'] = df.apply(replace_empty_with_mode, axis=1)

pivot_table = pd.pivot_table(df, values='Price', index=['Brand', 'VehicleType'], aggfunc='median')

pivot_table = pivot_table.sort_values(by='Price', ascending=False)

result_table = pivot_table.head(10).reset_index()

print(result_table)