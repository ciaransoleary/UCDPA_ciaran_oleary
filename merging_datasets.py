import pandas as pd

def print_dataframe_details(df_name = "Unnamed", dataframe=None):
	print("")
	print(df_name)
	print(dataframe.shape)
	print(dataframe.dtypes)


dropoutdata = pd.read_csv('dropoutdataprofileindicator.csv')
profilevalues = pd.read_csv('profilevalues.csv')

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
			"International",
			"Target"]:
    dropoutdata[i] = dropoutdata[i].astype('category')

profilevalues = profilevalues.iloc[:, 0:len(profilevalues.columns)].astype("category")

print_dataframe_details("Drop Out Data", dropoutdata)
print_dataframe_details("Profile Values", profilevalues)

merged_dropoutdata = dropoutdata.merge(profilevalues, left_on="Profile", right_on="Profile Indicator")
merged_dropoutdata = merged_dropoutdata.drop(["Profile"], axis=1)

print_dataframe_details("Merged Drop Out Data", merged_dropoutdata)

