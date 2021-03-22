import pandas as pd

data = pd.read_csv('./ch5/5-7/bmi.csv')
print(data)

data_keys = data.keys()
print(data_keys)
data_train = data[data_keys[0:2]]
data_label = data[data_keys[2]]
print(data_train)
print(data_label)