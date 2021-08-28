import import_dataset as id
df=id.import_dataset("city_temperature.csv")

print("we have cancelled the column State because it only contained Nans")
df.drop('State',axis='columns', inplace=True)
cleaned_df=df
print(cleaned_df)

print("we want to confirm that the year range goes from 1995-2020")
print(cleaned_df.Year.value_counts().index)

print("we count how many values we have for each year to understand how many values we have for 201 and 200")
print(cleaned_df.Year.value_counts())

print("we decide to remove 201 and 200 years because in total they count 440 values which is a very small number compared to the total number")
cleaned_df=cleaned_df[cleaned_df.Year>1990]
print(cleaned_df.Year.value_counts())

print("look for missing values")
print(cleaned_df.isna().sum())

print("replacing missing data")
cleaned_df["AvgTemperature"].fillna(method="ffill", inplace=True)
print(cleaned_df.isna().sum())