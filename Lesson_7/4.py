import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_percentage_error
from sklearn.preprocessing import OneHotEncoder

data = pd.read_csv("data.csv", delimiter=";", decimal=",")
data = data.dropna()


def replace_outliers(series):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 3 * iqr
    upper_bound = q3 + 3 * iqr
    outliers_index = series.index[(series < lower_bound) | (series > upper_bound)]
    median_value = series.median()
    series[outliers_index] = median_value
    return series


data['удой'] = data.groupby('порода')['удой'].transform(lambda x: replace_outliers(x))
data['Жирность,%'] = data.groupby('порода')['Жирность,%'].transform(lambda x: replace_outliers(x))
data["порода"] = data["порода"].replace({"РефлешнСоверинггггг": "РефлешнСоверинг"})

X = data[["протеин", "спо", "эке", "порода"]] 
y = data["удой"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42)


def create_spo_cat(X):
    X = X.copy()
    X["спо_кат"] = np.where(X["спо"] <= 0.9, "Низкое", "Высокое")
    return X.drop("спо", axis=1) 


X_train_processed = create_spo_cat(X_train)
X_test_processed = create_spo_cat(X_test)

encoder = OneHotEncoder(sparse=False)
X_train_encoded = encoder.fit_transform(X_train_processed[['порода', 'спо_кат']])
X_test_encoded = encoder.transform(X_test_processed[['порода', 'спо_кат']])

X_train_final = np.concatenate([X_train_processed.drop(['порода', 'спо_кат'], axis=1), X_train_encoded], axis=1)
X_test_final = np.concatenate([X_test_processed.drop(['порода', 'спо_кат'], axis=1), X_test_encoded], axis=1)

model = LinearRegression()
model.fit(X_train_final, y_train)
predictions = model.predict(X_test_final)

r2 = r2_score(y_test, predictions)
mape = mean_absolute_percentage_error(y_test, predictions) * 100

print(round(r2, 2), round(mape, 2))