import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
coviddata = pd.read_csv(r"C:\Users\amuda.sivaraj\PythonDatasets\13PythonDApractice\Covid_19_data.csv")
print(coviddata)
print(coviddata.count())
#Null values means missing values
print(coviddata.isnull().sum())

sns.heatmap(coviddata.isnull())
plt.show()

#Q1: Show the number of confirmed, Deaths and Recovered cases in each region.
#print(coviddata.head(2))

print(coviddata.groupby('Region').sum().head(20).to_string())

#print(coviddata.groupby('Region').sum().head(20))
print(coviddata.groupby('Region')['Confirmed'].sum().sort_values(ascending=False).head(20))

print(coviddata.groupby('Region')[['Confirmed', 'Recovered']].sum())

#Q2: Remove all the records where confirmed cases is less than 10

#print(coviddata[coviddata.Confirmed < 10])
#coviddata = coviddata[~(coviddata.Confirmed < 10)]  # to remove the records satisfying a particular condition
#print(coviddata.head(20))

#Q3 uses data where data is not removed : In which region, maximum number of confirmed cases were recorded?
print(coviddata)
print(coviddata.groupby('Region').Confirmed.sum().sort_values(ascending = False).head(20))

#Q4, In which region, minimum number of Death cases were recorded?
print(coviddata.groupby('Region').Deaths.sum().sort_values(ascending = True).head(50))

#Q5 How many confirmed, Death & Recovered cases were reported from India Till 29th April 2020?
print(coviddata[coviddata.Region == 'US'])

#Q6A:Sort the entire data wrt no.of confimred cases in ascending order
print(coviddata.sort_values(by= ['Confirmed'] , ascending = True))
#Q6B:ort the entire data wrt no.of recovered cases in descending order

print(coviddata.sort_values(by= ['Recovered'] , ascending = False))
