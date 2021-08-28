import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.layouts import row

##################dataset cleaning#####################################

import import_dataset as id
df=id.import_dataset("city_temperature.csv")

print("we have cancelled the column State because it only contained NaNs")
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

######################dataset elaboration#######################

print("converting the dataset containing Fahrenheit temperatures in Celsius")
cleaned_df["celsius"]=(cleaned_df["AvgTemperature"] - 32) * 5/9
print(cleaned_df.head())

print("checking the average temperature of regions between 1995 and 2020 using groupby function")
print(cleaned_df[['Region','celsius']].groupby('Region').mean().sort_values(by='celsius', ascending=False))


print("checking the yearly average temperatures of regions")
df_region = cleaned_df[['Region','Year','celsius']].groupby(['Region','Year']).mean().reset_index()
print(df_region.head())
print(df_region)

print("now we show the yearly average of regions temperature trend plotting it")
sns.relplot(x="Year", y="celsius", data=df_region, kind="line",style="Region", hue="Region")
plt.show()


print("comparing the average temperature between 1995 and 2019 ignoring 2020 as not completed yet")
avg_temp=cleaned_df[cleaned_df.Year.isin([1995,2019])][['Region','Year','celsius']].groupby(['Region','Year']).mean().reset_index()
print(avg_temp)


print("plotting the average temperature between 1995 and 2019")
sns.catplot(x="Year", y="celsius", data=avg_temp, kind="bar", hue="Region")
plt.show()


print("comparing the average monthly temperatures of regions")
df_region2 = cleaned_df[['Region','Month','celsius']].groupby(['Region','Month']).mean().reset_index()
print(df_region2)

print("plotting the average monthly temperatures of regions, please wait it might take up to 120 sec to run")
sns.relplot(x="Month", y="celsius", data=cleaned_df, kind="line", style="Region", hue="Region", markers=True)
plt.show()


print("comparing the hottest and coldest city in the world")
df_city=cleaned_df[['City','celsius','Country']].groupby(['City','Country']).mean().sort_values(by='celsius',ascending=False).reset_index()
print(df_city)


print("plotting the hottest and coldest city in the world")
sns.relplot(x="Month", y="celsius", data=df_region2, kind="line", hue="Region")
plt.show()

print('example of application of Numpy + Matplotlib')
print('We want to produce a bar plot with Matplotlib to show average temperatures over 1995 till 2020')
print('for just two states, let’s say Europe and North America')
europe_temperatures=df_region[(df_region["Region"]=="Europe")]
labels=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
print("first print")
print(europe_temperatures)
eu_temp=europe_temperatures[["celsius"]]
print("second print")
print(type(eu_temp))
eu_temp=eu_temp.to_numpy()
print("third print")
print(eu_temp)
eu_temp=np.transpose(eu_temp)
eu_temp=eu_temp[0]
print("fourth print")
print(eu_temp)
print(eu_temp.shape)


print('North America')
n_america_temperatures=df_region[(df_region["Region"]=="North America")]
n_am_temp=n_america_temperatures[["celsius"]]
n_am_temp=n_am_temp.to_numpy()
n_am_temp=np.transpose(n_am_temp)
n_am_temp=n_am_temp[0]


print('plotting the two numpy arrays we just created')
x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, eu_temp, width, label='Europe')
rects2 = ax.bar(x + width/2, n_am_temp, width, label='North America')
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Temp [C]')
ax.set_title('Yearly Average Temperatures in Europe and North America ')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
fig.tight_layout()
plt.show()

print("plotting with bokeh average temperature of Europe and North America from 1995 to 2020")
p1=figure(x_axis_label="Year", y_axis_label="celsius")
p1.line(labels,eu_temp, color="blue")
p1.circle(labels, eu_temp, color="blue", size=10,line_color="white" , legend_label="Europe")
# display legend in top left corner (default is top right corner)
p1.legend.location = "top_left"
p2=figure(x_axis_label="Year", y_axis_label="celsius")
p2.line(labels,n_am_temp, color="red")
p2.circle(labels, n_am_temp, color="red", size=10,line_color="white" , legend_label="North America")
# display legend in top left corner (default is top right corner)
p2.legend.location = "top_left"
layout=row(p1,p2)
output_file('average_temperature_europe_vs_north_america.html')
show(layout)
