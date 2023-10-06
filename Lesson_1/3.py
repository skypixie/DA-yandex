import pandas as pd


df = pd.read_csv('data3.csv', sep=',')
new_df = df['возраст'].apply(lambda x: ('менее_30' if x <= 30 else 'более_30')).rename('возраст_кат')
age_category = new_df.value_counts(normalize=True).apply(lambda x: round(x * 100))

print(age_category.to_frame())