import pandas as pd
data = pd.read_csv(r"C:\Users\amuda.sivaraj\PythonDatasets\13PythonDApractice\Project+7+-+Udemy+Dataset.csv")
print(data)

#1 what are all different subject for which Udemy is offering courses?
print(data.columns)
#syntax: data.subject.unique()
print(data.subject.unique())
#2 which subject has maximium number courses
print(data.subject.value_counts())

#3 Show all the courses which free of cost
print(data[data.is_paid == False])

#4 Show all courses which are paid
print(data[data.is_paid == True])
#5 which are top selling courses
#pd.set_option('display.max_columns', None)  # show all columns
sorted_data = data.sort_values('num_subscribers', ascending=False)

print(sorted_data)

#6 which are least selling courses
data.sort_values('num_subscribers')

#7Show all courses of graphic design where the price is below 100?
print(data[(data.subject == 'Graphic Design') & (data.price < '100')])
#print(data[(data.subject == 'Graphic Design') & (data.price == '100')])
#8 List out all the courses that are related to python
#print(data[data.course_title.str.contains('Python')])
# or
print(len(data[data.course_title.str.contains('Python')]))

#9 what are courses that are published in year 2015?
print(data.dtypes)
#now convert published_timestamp datetime
data['published_timestamp']=pd.to_datetime(data.published_timestamp)
print(data.dtypes)
#add new column 'Year'
data['Year'] = data['published_timestamp'].dt.year

data = data[data.Year == 2015]
print(data)

#10 what are the max number subcriber for each level of courses
data =data.groupby('level')['num_subscribers'].max()
print(data)
data = data.groupby('level').max()
print(data)

