import pandas as pd
import numpy as np

def print_dataframe_details(df_name = "Unnamed", dataframe=None):
	print("")
	print(df_name)
	print(dataframe.shape)
	print(dataframe.dtypes)

dropoutdata = pd.read_csv('dropoutdata.csv')

for i in ["Marital status", 
		"Application mode", 
		"Application order", 
		"Course", 
		"Daytime/evening attendance", 
		"Previous qualification", 
		"Nacionality", 
		"Mother's qualification", 
		"Father's qualification", 
		"Mother's occupation", 
		"Father's occupation", 
		"Displaced", 
		"Educational special needs", 
		"Debtor", 
		"Tuition fees up to date", 
		"Gender", 
		"Scholarship holder", 
		"International", 
		"Target"]:
	dropoutdata[i] = dropoutdata[i].astype('category')

rng = np.random.default_rng(28062023)
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

print("Before...")
print(dropoutdata.isnull().sum())


columns_with_missing_values = dropoutdata.columns[dropoutdata.isna().any()]

for col in columns_with_missing_values:
	if(dropoutdata[col].dtype == "category"):
		dropoutdata[col].fillna(dropoutdata[col].value_counts().index[0], inplace = True)
	elif (dropoutdata[col].dtype == "int64" or dropoutdata[col].dtype == "float64"):
		dropoutdata[col].fillna(dropoutdata[col].mean(), inplace = True)

print("After...")
print(dropoutdata.isnull().sum())
