import pandas as pd

#created a dictionaries that contains a list
region={
    'Region':['Europe','Africa','Asia','South/Central America','Australia/South Pacific','Middle East'],
    'Country':['Italy','Angola','Asia','Argentina', 'Australia','Turkey']
}
names={
    'Region':['Europe','Africa','Asia','South/Central America','Australia/South Pacific','Middle East'],
    'Abbreviation':['IT','AO','JP','AR','AU','TR']

}
#converted the dictionary into dataframe
df1=pd.DataFrame(region)
df2=pd.DataFrame(names)

# code to merge two dataframes
df=pd.merge(df1,df2, on='Region')
print(df)