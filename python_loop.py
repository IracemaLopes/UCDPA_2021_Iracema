import pandas as pd
#created a dictionary
dict={ 'name':['Lisa','Mark','Joe','Eva'],
       'degree':['MBA', 'BCA', 'TECH','MATH'],
       'score': [100,95,89,91]}
#converted the dictionary into dataframe
df=pd.DataFrame(dict)

#iterate through each row of dataframe
for lab, row in df.iterrows():
    print(lab)
    print(row)