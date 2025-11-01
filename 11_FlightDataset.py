import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline  note:only works in IPython environments like Jupyter Notebook or Jupyter Lab.
import seaborn as sns
plt.xticks(rotation=45) 
data = pd.read_csv(r"C:\Users\amuda\13DataAnalysisProject\11. airlines_flights_data.csv")
pd.set_option('display.max_columns', None)
print(data)
#cleaning the data
#First column is index column we can remove
data.drop(columns = 'index', inplace = True)
print(data.info())
# Get Statistical summary about the dataset
print(data.describe())
#confirm the max  from flight details
print(data[data['duration'] == 49.830000])
#confirm the min from flight details
print(data[data['duration']== 0.830000])
#simlarly we can find result for price or days left


#check for null values
print(data.isnull().sum())
#Q1: What are the airlines in the dataset, accompanined by their frequencies?
# Checking how many Airlines are in the dataset
print(data.head())
print(data['airline'].nunique())
print(data['airline'].unique())
# Showing all the Airlines with their frequencies
print(data['airline'].value_counts())
# Showing all the Airlines with their Number of Flights in Horizontal Bar Graph
data['airline'].value_counts(ascending=True).plot.barh(color=['green', 'lightgreen'])
plt.title('Airlines with frequencies')
plt.xlabel('Number of flights')
plt.ylabel('Airline')
plt.show()

#Q2: Show Bar graphs representing the departure Time & Arrival
print(data['departure_time'].value_counts())
print(data['arrival_time'].value_counts())
plt.figure(figsize=(14,4))

#Create to subplot one for departure and 2nd for arrival 
plt.subplot(1,2,1)
plt.bar(data['departure_time'].value_counts().index,data['departure_time'].value_counts().values, color= ['r', 'b'])
plt.title("Departure Time")   
plt.xlabel("D Yime")    
plt.ylabel("D Frequency")  
#plt.show()   Note when you habe subplot only once we plt.show()

plt.subplot(1,2,2)           
plt.bar(data['arrival_time'].value_counts().index,data['arrival_time'].value_counts().values,color=['g','y'])
plt.title("Arrival Time")
plt.xlabel("A Time")
plt.ylabel("A Frequency")
plt.show()


#Q3: Show Bar Graphs representing the source city & Distination city
print(data['source_city'].value_counts())
print(data['destination_city'].value_counts())
plt.figure(figsize=(16,4))
#Create to subplot one for source city and 2nd for Distination city
plt.subplot(1,2,1)
plt.barh(data['source_city'].value_counts().index, data['source_city'].value_counts().values, color = ['r', 'y'])
plt.title("Source Cities with No. of flights")
plt.xlabel("Cities")
plt.ylabel("No.of flighs")

plt.subplot(1,2,2)
plt.barh(data['destination_city'].value_counts().index, data['destination_city'].value_counts().values, color = ['b', 'm'])
plt.title("Destination Cities with No. of flights")
plt.xlabel("Cities")
plt.ylabel("No.of flighs")
plt.show()


#Q4: Does price varies with airlines? Yes
print(data.groupby('airline')['price'].mean())
#draw catgorical plot using sns
sns.catplot(x = 'airline', y = 'price', kind = 'bar', palette= 'rocket',data=data, hue='class')
plt.show()

#Q5. Does ticket price change based on the departure time and arrival time?
print(data.groupby('departure_time')['price'].mean())
print(data.groupby('arrival_time')['price'].mean())

sns.catplot(x='departure_time', y = 'price', kind ='bar',data=data)
plt.show()
sns.catplot(x='arrival_time', y = 'price', kind ='bar',data=data)
plt.show()
sns.relplot(x='arrival_time', y='price',data=data,col ='departure_time',kind = 'line')
plt.show()
#Q6: How the price changes with changes in source and destination? yes
data.groupby('source_city')['price'].mean()
data.groupby('destination_city')['price'].mean()
sns.relplot(x='destination_city', y='price',data=data,col ='source_city',kind = 'line')
plt.show()
#Q7: How is the price affected when the tickets are bought in just 1 or 2 days before departure?closer departure prices are high
print(data['days_left'].nunique())
print(data['days_left'].unique())
print(data.groupby('days_left')['price'].mean())
sns.relplot(x='days_left', y='price', data=data, kind = 'line')
plt.show()

#Q8: How does the ticket price vary between Economy and Business class?
print(data['class'].nunique())
print(data['class'].unique())

# Filtering out the records with Economy class

x = data [ data['class'] == 'Economy' ]
# Checking Mean Price for Economy class tickets

x.price.mean()
print(x.price.mean())

# Filtering out the records with Business class

y = data [ data['class'] == 'Business' ]
# Checking Mean Price for Business class tickets

print(y.price.mean())
#Q9: what will be the Average price of Vistara airline for a flight from delhi to hyderabad in business class?
new_data=data[(data['airline']=='Vistara')&(data['source_city']=='Delhi') &(data['destination_city']=='Hyderabad') & (data['class']== 'Business')]
print(new_data['price'].mean())
