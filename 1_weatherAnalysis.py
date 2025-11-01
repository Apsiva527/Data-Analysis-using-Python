import pandas as pd
data = pd.read_csv(r"C:\Users\amuda\13DataAnalysisProject\Project+1+-+Weather+Dataset.csv")
print(data)
print(data.head())
print(data.shape)
data.index
data.columns
data.dtypes
#now findout uniques values of particular colum
print(data['Weather'].unique())
print(data.nunique())
print(data.count())
print(data['Weather'].value_counts())
print(data.info())
#1.Find all the uniuqe "wind speed values in the data
print(data['Wind Speed_km/h'].unique())  #Answer
print(data['Wind Speed_km/h'].nunique())
# 2.Find the number of times when the weather is excatly clear
#1.Get value_count(),  
print(data['Weather'].value_counts())
print(data.Weather.value_counts())
#2. filtering
print(data[data.Weather == 'Clear'])
#3. group by
print(data.groupby('Weather').get_group('Clear'))

# 3.Find the number of times when the 'Wind Speed was excatly 4 km/h we can use filter
print(data[data['Wind Speed_km/h'] == 4])  #Answer
#4.Find out the null valaues in the data: 2ways
    #using isnull
print(data.isnull().sum())
    #using not null function
    # 
print(data.notnull().sum())

#5 Rename the column name 'Weather' of the dataframe to weather condition'.
print(data.rename(columns = {'Weather' : 'Weather Condition'}, inplace = True))
print(data.head(2))

#6 what is the mean 'Visibility'?
print(data.Visibility_km.mean())

#7 what is the standard deviation of "Pressure" in this data?
print(data.Press_kPa.std())
#8 what is the variance of "Relative Humidity" in this data?
print(data['Rel Hum_%'].var())  #here we have used square bracket becasue the name having space then we need to put th square bracket

#9Find all instances when 'Snow' was recorded
#3 ways, 1. value_counts(), 2.Filtering,3. str.contains
print(data['Weather Condition'].value_counts())
#filtering
print(data[data['Weather Condition']=='Snow'])
#str.contains
print(data[data['Weather Condition'].str.contains('Snow')])

#10 Find all instances when 'Wind speed is above 24' and visibility is 25'
print(data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)] )

#11.what is the mean value of each of each column against each 'Weather Condition?
#print(data.groupby('Weather').get_group('Clear'))
# 
result = data.groupby('Weather Condition').mean(numeric_only=True)
print(result)

#12 what is minimum & Maximum value of each column against each 'Weather condition'?

print(data.groupby('Weather Condition').min())
print(data.groupby('Weather Condition').max())
#13 show all the records where Weather condition is fog
print(data[data['Weather Condition'] == 'Fog'])

#14 Find all instances when 'Weather is clear' or Visibiltyt is above 40'
print(data[(data['Weather Condition']== 'Clear') | (data['Visibility_km'] > 40)].tail(50))

#15 Find all instances when:
#A.'Weather is clear and "relative humidity is greater than 50"

# or
#B.Visibilty is above 40'

print(data[((data['Weather Condition'] == 'Clear') & (data['Rel Hum_%'] > 50)) | (data['Visibility_km'] > 40)])






