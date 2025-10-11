import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv(r"C:\Users\amuda.sivaraj\PythonDatasets\13PythonDApractice\Netflix+Dataset.csv")
#print(data)
print(data.head(3)) # to show top 5 records of the dataset
print(data.tail(3)) # to show bottom 5 records of dataset
print(data.shape) # to show the no.of rows and columns
print(data.size) # to show no of total values(elements ) in the datast
print(data.columns)  #To show each column names
print(data.dtypes)  # to show the data type of each column
print(data.info())  # to show datatypes of each columns
print(data['Director'].unique())#unique() returns all the unique/distinct values from a Series (one column of a DataFrame).
print(data['Country'].nunique()) #nunique() returns the number of unique/distinct values in a Series (column) or across the whole DataFrame.
# Task 1. Is there any Duplicate record in this dataset ? If yes, then remove the duplicate records
#1 Get nuber of duplicates
print(data[data.duplicated])
#2. Remove duplicate
print(data.drop_duplicates(inplace = True))
print(data)

#Task2. Is there any Null value present in any column ? show with Heat-map?
print(data.isnull().sum())
sns.heatmap(data.isnull())
plt.show()

#Q1:For 'House of Cards, what is the show id and who is the director of this show?
#titles = data['Title'].tolist()
#print(titles)
#print(data[data['Title'].isin(['House of Cards'])])    #using isin()
print(data[data['Title'].str.contains('House of Cards')])  #using str.contains


#Q2:In which year highest number TV shows & movies were released? Show with Bar Graph
print(data.dtypes)
data['Release_Date'] = data['Release_Date'].str.strip()
data['Date_N'] = pd.to_datetime(data['Release_Date'])
print(data.dtypes)

print(data['Date_N'].dt.year.value_counts())   # it counts the occurance of all indiviual years in Date column
data['Date_N'].dt.year.value_counts().plot(kind='bar')
plt.show()



#3 How many movies and TV shows are in dataset / Show with Bar graph

print(data.groupby('Category').Category.count())  # To group all unique items of a column and show their count


#sns.countplot(data['Category'])
sns.countplot(x='Category', data=data, palette='Set2')    # To show the count of all unique values of any column in the form of bar graph
plt.show()

#4 show all movies that were released in year 2000
data['Year'] = data['Date_N'].dt.year
print(data.head(2))
print(data[(data['Category'] == 'Movie') & (data['Year'] == 2000)])
#let say 2020

print(data[(data['Category'] == 'Movie') & (data['Year'] == 2020)])

#5how only only tiles of all TV shows that released in India only
print(data[(data['Category'] == 'TV Show') & (data['Country'] == 'India')]['Title'])


#6 Show top 10 directors, who gave highest number TV shows and movies to netflix?
print(data['Director'].value_counts().head(10))

#7 Show all the records where "category" is movie and type comedies or country is "United Kingdom"

#data[ (data['Category']=='Movie') & (data['Type']=='Comedies') | (data['Country']=='United Kingdom')]
print(data[(data['Category'] == 'Movie') & ( data['Type'] == 'Comedies') | (data['Country'] == 'United Kingdom')])

#8 In how many movies/shows, 'Tom Cruise' is cast?
print(data[data['Cast']== "Tom Cruise"])  # This is not right because multiple element in a column
# We can use str.contains function to get the result but str.contains cannot be applied on null values, so we need to remove all null values

data_new = data.dropna()    # It drops the rows that contains all or any missing values.
pd.set_option('display.max_columns', None)
print(data_new[data_new['Cast'].str.contains('Tom Cruise')])

#9 what are different rating is defined by Netflix?
print(data['Rating'].nunique())
print(data['Rating'].unique())

    #9.1 How movies got the TV-14 rating in Canada?
print(data[(data['Category'] =='Movie') & (data['Rating']=='TV-14')  & (data['Country'] =='Canada')].shape)
    #9.2 How many TV show got R rating after year 2018
print(data[(data['Category'] =='TV Show') & (data['Rating'] == 'R') & (data['Year'] > 2018)])


#10 what is maximum duration of movie/shows on Netflix?
data.Duration.unique()
data.Duration.dtypes

#Since it is data type is 'Object' , convert this minitues
data[['Minutes', 'Unit']] = data['Duration'].str.split(' ', expand = True)
print(data.head(2))

#Now we can easliy find max duration which is in min
print(data['Minutes'].max())
print(data['Minutes'].min())

#11 which individual country has highest no. of TV shows?
data_tvshow = data[data['Category']=='TV Show']

print(data_tvshow.head(2))

print(data_tvshow.Country.value_counts().head(1))

#12 How can we sort the dataset by Year 
print(data.sort_values(by = 'Year', ascending=False))

#13 Find all the instances where
print(data [(data['Category']=='Movie') & (data['Type']=='Dramas')].head(2))
 #Category is movie and type is Drama
print(data [ (data['Category']=='TV Show') & (data['Type']== "Kids' TV") ])
 # or
 # Category is TV show & type is kids TV
print(data [ (data['Category']=='Movie') & (data['Type']=='Dramas') | (data['Category']=='TV Show') & (data['Type']== "Kids' TV") ])
 

