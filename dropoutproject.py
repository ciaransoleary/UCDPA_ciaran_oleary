import pandas as pd
import numpy as np

dropoutdata = pd.read_csv('dropoutdata.csv')

rng = np.random.default_rng(2706202312)
number_of_columns_to_set_to_include_missing_values = int(rng.random() * (len(dropoutdata.columns) - 1))
columns_to_set_to_include_missing_values = (rng.random(size = number_of_columns_to_set_to_include_missing_values) * (len(dropoutdata.columns) - 1))
columns_to_set_to_include_missing_values = list(map(lambda x: int(x), columns_to_set_to_include_missing_values))

max_number_of_values_to_set_to_missing_in_any_column = int(rng.random() * (len(dropoutdata) / 100))
number_of_values_to_set_to_missing_in_identified_columns = []
for i in range(0, number_of_columns_to_set_to_include_missing_values):
	number_of_values_to_set_to_missing_in_identified_columns.append(int(rng.random() * max_number_of_values_to_set_to_missing_in_any_column))

for i in range(0, number_of_columns_to_set_to_include_missing_values):
	for j in range(0, number_of_values_to_set_to_missing_in_identified_columns[i]):
		row_index_for_this_column_to_set_to_missing = int(rng.random() * (len(dropoutdata) - 1))
		dropoutdata.iloc[row_index_for_this_column_to_set_to_missing, columns_to_set_to_include_missing_values[i]] = np.NAN

print("Number of columns to set to include missing values      :", number_of_columns_to_set_to_include_missing_values)
print("Columns to set to include missing values                :", columns_to_set_to_include_missing_values)
print("Number of values to set to missing in identified columns:", number_of_values_to_set_to_missing_in_identified_columns)

print(dropoutdata.isnull().sum())
