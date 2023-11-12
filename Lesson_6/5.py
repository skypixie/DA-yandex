import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
 
data = pd.read_csv('data.csv') 
df = pd.DataFrame(data) 
df.columns = [col.lower().replace(' ', '_') for col in df.columns] 
 
 
def categorize_year(year): 
    if year <= 1980: 
        return 'раритет' 
    elif year <= 2010: 
        return 'старые' 
    elif year <= 2020: 
        return 'массовые' 
    else: 
        return 'современные' 
 
     
df['age_group'] = df['registrationyear'].apply(categorize_year) 
 
 
def filter_data(brand): 
    filtered_data = df[(df['brand'] == brand) & (df['power'] > 30) & (df['price'] > 0)] 
    return filtered_data 
 
 
selected_brand = input() 
selected_data = filter_data(selected_brand) 
 
fig, axes = plt.subplots(1, 3, figsize=(11, 4)) 
 
selected_data['age_group'].value_counts().plot(kind='pie', ax=axes[0], autopct='%1.1f%%',) 
 
axes[0].set_title('Возраст автомобиля') 
 
sns.histplot(selected_data['price'], bins=20, ax=axes[1], kde=True) 
 
axes[1].set_title('Цена') 
axes[1].set_xlabel('Цена', fontsize=13) 
 
sns.scatterplot(x='power', y='price', data=selected_data, ax=axes[2]) 
 
axes[2].set_title('Мощность vs Цена') 
axes[2].set_xlabel('Мощность', fontsize=13) 
 
fig.suptitle('Исследование данных по моделям автомобилей', fontsize=16, y=1.01) 
 
plt.savefig('target_6_5.png')