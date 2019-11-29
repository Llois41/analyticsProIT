import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 5000)
data = pd.read_csv('..\data\listings.csv')

for data_row in data.columns.values:
    print(data_row)