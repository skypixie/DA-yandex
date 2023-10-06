import pandas as pd
import numpy as np


df = pd.read_csv('data.csv', sep=';').replace(r'^\s*$', np.nan, regex=True).dropna()
print(*df.shape)