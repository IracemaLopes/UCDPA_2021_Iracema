import import_dataset as id
df=id.import_dataset("city_temperature.csv")
#returns the first few rows of the head of the Dataframe
print(df.head())

#shows infor on each of the columns, such as data type and number of missing values.
print(df.info())

#returns the number of rows and columns of the DataFrame
print(df.shape)

#calculating a few summary statistics for each column
print(df.describe())