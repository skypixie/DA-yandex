import pandas as pd


def decide_distance_category(dist: int):
    if (dist <= 300):
        return 'домашний_регион'
    elif (dist <= 700):
        return 'недалеко_отдома'
    else:
        return 'дальнее_путешествие'


df = pd.read_csv('data4.csv', sep=',')

distance_df = df['расстояние'].apply(lambda x: decide_distance_category(x))
distance_series = distance_df.rename('расстояние_кат').value_counts(normalize=True)
print(distance_series.apply(lambda x: round(x * 100)).to_frame())
