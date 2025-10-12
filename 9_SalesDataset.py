import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_excel(r"C:\Users\amuda.sivaraj\PythonDatasets\13PythonDApractice\Sales-Data-Analysis.xlsx")
print(data)
print(data.info())
#CLEANING THE DATA drop unwanted column,changing column names, removing duplicate records, converting datatypesof the columns
data.drop(columns='Unnamed: 0', inplace = True)  # to drop the column from the dataframe
print(data.head())
print(data.loc[0])   
print(data.columns)                      # using the loc function to show Ist row values
data.columns = data.loc[0]
print(data)
#DROP UNWANTTED ROW
data.drop(0, inplace = True)
print(data.info())
print(data.Manager)
print(data.Manager.unique)
data['Manager'] = data['Manager'].str.strip().str.replace(r'\s+', ' ', regex=True)   # to remove extra spaces in names
print(data.head(20))
print(data['Manager'].unique())# to show all the unique values of the column
print(data['Manager'].nunique())#to show count of unique values present in the column
#removing duplicate
print(data[data.duplicated()])  # to show all the duplicate records
data.drop_duplicates(inplace=True) 
print(data)        # to remove the duplicate records

print(data.describe())

print(data[data['Order ID'].duplicated()])        # to check the duplicate records in a column


print(data[data['Order ID'] == 10483])

print(data[data['Order ID'] == 10484])          # using filtering to show some records

print(data[data['Order ID'].duplicated()]) 
print(data)
print(data.info()) 

data.Quantity = data.Quantity.astype(float)  # to change the datatype of a column
print(data.info())
print(data['Quantity'].dtype)
data.Quantity = data.Quantity.round()  # to round-off the values of a column
print(data.Quantity)

data.Quantity = data.Quantity.astype(int)  # to change the datatype of a column
print(data.Quantity)
data['Order ID'] = data['Order ID'].astype(int)
data.Price=data.Price.astype(float)
print(data.info())

data.Date = pd.to_datetime(data.Date)  # to convert the datatype into datetime format
print(data.Date.dtype)
print(data.info())

print(data)

#ANALYSIZING THE DATA


#1.Most Preffered Payment method
print(data['Payment Method'].unique())  # to show the unique values of a column

print(data['Payment Method'].nunique())   # to show the count of unique values in a column

print(data['Payment Method'].value_counts()) # to show the unique values of a column with their counts
print(data['Payment Method'].value_counts(normalize= True) * 100)  # to get the result in percentage
data['Payment Method'].value_counts().plot(kind = 'bar');
plt.show()

#2: MOst selling Product
#BY QUANTITY
print(data.groupby('Product')['Quantity'].sum())
#data.groupby('Product')['Quantity'].sum().sort_values(ascending= False)  # to sort the result

most_quantity = data.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
print(most_quantity)
print(type(most_quantity))  #'pandas.core.series.Series
most_quantity = most_quantity.reset_index()     # To convert the index of a Series into a column to form a DataFrame


# Create chart
plt.figure(figsize = (9,4))
plt.bar(most_quantity['Product'], most_quantity['Quantity'], color=['red','black','green', 'yellow', 'cyan'], width=0.4)
plt.title("Most Selling Product - By Quantity")              
plt.xlabel("Product")
plt.ylabel("Quantity");
plt.show()
#By revenue
data['Revenue'] = data['Price'] * data['Quantity']       # to create a new column 'Revenue'
print(data)

most_revenue = data.groupby('Product')['Revenue'].sum().sort_values(ascending= True) # to make the group of unique values of a column


print(type(most_revenue)) #pandas.core.frame.DataFrame
most_revenue = most_revenue.reset_index()     # To convert the index of a Series into a column to form a DataFrame
print(most_revenue)

plt.figure(figsize=(9, 4))
plt.bar(most_revenue['Product'], most_revenue['Revenue'], color = ['green', 'red', 'black', 'yellow', 'cyan'], width = 0.3);
plt.title("Most Selling Product - By Revenue")       # setting the title       
plt.xlabel("Product")                                # setting the x-axis label
plt.ylabel("Revenue");                               # setting the y-axis label
plt.show()



#3 Which city had maximum revenue or which manager earned maximum revenue
#CITY
print(data.City.unique()) #get uniuqe city
print(data.City.nunique()) #get nunique city
print(data.groupby('City')['Revenue'].sum().sort_values(ascending=False))

#Manager
print(data.Manager.unique()) #get uniuqe Manager
print(data.Manager.nunique()) #get nunique Manager
print(data.groupby('Manager')['Revenue'].sum().sort_values(ascending=False))

#4: Date wise revenue

print(data.Date.dtype)
print(data.info())
data.plot('Date','Revenue',color='cyan', linewidth=2, figsize=(9,4))
plt.title("Date wise Revenue")       # setting the title       
plt.xlabel("Date")                                # setting the x-axis label
plt.ylabel("Revenue");                               # setting the y-axis label
plt.show()

#5 Average revenue
print(data.Revenue.mean())

#6:Average revenue of november and december month
data['Month'] = data['Date'].dt.month        # creating a new column showing Month only
print(data.info())
#filtering Month 11
m11 = data[data['Month'] ==11]
print(m11.Revenue.mean())

# same for month 12
m12 = data[data['Month']== 12]
print(m12.Revenue.mean())


#7:Standard deviation of revenue and quantity
print(data['Revenue'].std())

print(data['Quantity'].std())
#8 Variance of revenue and quantity
print(data['Revenue'].var())

print(data['Quantity'].var())

#9: Is revenue increasing or decrease over time?
print(m11.Revenue.sum())
print(" ")
print(m12.Revenue.sum())


#10: Average quantity sold and Average revenue for each product?
#Avg_productsold = data.groupby('Product')['Quantity','Revenue'].agg({'Quantity' : 'mean','Revenue' : 'mean'})
data.groupby('Product').agg({'Quantity': 'mean', 'Revenue': 'mean'})  # using agg() with groupby
#print(Avg_productsold)
