import pandas as pd
data= pd.read_csv(r"C:\Users\amuda.sivaraj\PythonDatasets\13PythonDApractice\3. Police Data.csv")
print(data)


#Remove columns that have only missing columns
print(data.columns)
print(data.isnull().sum())
data.drop(columns = 'country_name', inplace = True)
pd.set_option('display.max_columns', None)
print(data)

#Question(Based on Filtering + Value counts)
#2. For Speeding, were Men or Women stopped more often?
# df[df.Column_1 == 'Element/Value'].Column_2.value_counts()

print(data[data.violation=='Speeding'].driver_gender.value_counts())

#Question(groupby)
# 3. Does gender affect who gets searched during a stop?
# df.groupby('Column_1').Column_2.sum()
print(data.groupby('driver_gender').search_conducted.sum())
print(data.search_conducted.value_counts())

#Question(Mapping + data_type casting)
#4 what is the mean stop_duration?
# df['Column_name'] = df['Column_name'].map( { old:new , old:new} )

# df['Column_name'].mean()
print(data.stop_duration.value_counts())
data['stop_duration'] = data['stop_duration'].map({'0-15 Min': 7.5,'16-30 Min' : 24,'30+ Min' : 45 })
print(data['stop_duration'].mean())

#Question(groupby, describe)
#5.Compare the age distributions for each violation

# df.groupby('Column_1').Column_2.describe()
print(data.groupby('violation').driver_age.describe())

a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

import numpy as np
np.mean(a)