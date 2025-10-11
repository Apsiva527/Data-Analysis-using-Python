import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
LH= pd.read_csv(r"C:\Users\amuda.sivaraj\PythonDatasets\13PythonDApractice\Housing+Data.csv")
print(LH)

#1.
print(LH.count())
print(LH.isnull().sum())

# 2.

sns.heatmap(LH.isnull())
plt.show()

#A: Convert the datatype of date column to Date-Time format

print(LH.dtypes)
#print(LH.date = pd.to_datetime(LH.date))

print(LH.columns)
LH.date = pd.to_datetime(LH.date)
print(LH.dtypes)
#B1. Add a new column "year" in the dataframe, which contains years only
LH['year'] = LH.date.dt.year
print(LH)
#B2 Add anew column "month" as 2nd column in the dataframe, which contains month only

LH.insert(1, 'month', LH['date'].dt.month)

print(LH)
#C: Remove column year and month from the dataframe
LH.drop( ['month' , 'year'] , axis=1 , inplace = True )
print(LH)
#D show all the columns where no of crimes are 0 And how many such records are there?
print(len(LH[LH.no_of_crimes == 0]))
#5 what is the maximum and minimum average price per year in england?
LH['year'] = LH.date.dt.year
print(LH)
#print(LH.head(2))
#apply filter to get England

df1=LH[LH.area == 'england']
print(df1)

#print(df1.groupby('year').average_price.max())

#print(df1.groupby('year').average_price.min())

print(df1.groupby('year').average_price.mean())
#6what is the maximum and minimum no of crimes per area in england?
#print(LH.groupby('area').no_of_crimes.max())
print(LH.groupby('area').no_of_crimes.min().sort_values(ascending=False))


#7. Show the total count of records of each area, where average price is less than 100000

print(LH[LH.average_price < 100000].area.value_counts())