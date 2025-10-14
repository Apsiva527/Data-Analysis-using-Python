import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv(r"C:\Users\amuda.sivaraj\PythonDatasets\13PythonDApractice\ai_financial_market_daily_realistic_synthetic.csv")
print(data)
# Show basic information about the data
print(data.info())
# Convert datatype of Date column into DataTime format
data['Date'] =pd.to_datetime(data['Date'])
print(data.info())
print(data.head())
print(data['Company'].unique())
print(data['Company'].nunique())
# Create a new column for 'Year' only
data['Year'] = data['Date'].dt.year
print(data.info())
print(data.isnull().sum())
print(data.head())


#How much amount the companies spent on R & D?
print("Companies spending for R & D in $Bn")
RD =data.groupby('Company')['R&D_Spending_USD_Mn'].sum()/1000  #convert the value billion by didviding by 1000
print(RD)
# Draw a Bar Plot to show the amount spent on R & D by the companies
plt.bar(RD.index,RD.values,color=['cyan','black','magenta'])
plt.title("R&D Spending by the companies")
plt.xlabel("Companies")
plt.ylabel("Amount in USD$Bn")
plt.show()
#Revenue Earned by the companies
print("Companies Revenue earned in $Bn")
Rev=data.groupby('Company')['AI_Revenue_USD_Mn'].sum()/1000
print(Rev)

plt.bar(Rev.index, Rev.values, color = ['yellow','red', 'green'], width=0.2)
plt.title("Revenue earned by the companies")
plt.xlabel("Companies")
plt.ylabel("Revenue earned in $Bn")
plt.show()

# We can same in same graph using subplot function
# Bar plots to show expenditure & revenue of the companies
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.bar(RD.index,RD.values,color=['cyan','black','magenta'])
plt.title("R&D Spending by the companies")
plt.xlabel("Companies")
plt.ylabel("Amount in USD$Bn")


plt.subplot(1,2,2)
plt.bar(Rev.index, Rev.values, color = ['yellow','red', 'green'], width=0.2)
plt.title("Revenue earned by the companies")
plt.xlabel("Companies")
plt.ylabel("Revenue earned in $Bn")
plt.show()

#Datewise Impact on the stock
plt.figure(figsize=(10,5))
plt.plot(data["Date"],data["Stock_Impact_%"], color='green')
plt.title("Change in Stock value")
plt.xlabel("Date ('Year')")
plt.ylabel("Stock_Impact_%")
plt.show()
#Create 3 spearate dataframes
data_Openai = data[data['Company'] == 'OpenAI']
print(data_Openai)
print(" ")
plt.figure(figsize=(10,4))
plt.plot(data_Openai['Date'],data_Openai["Stock_Impact_%"], color='m')
plt.title("Change in Stock value of OpenAI")
plt.xlabel("Date ('Year')")
plt.ylabel("Stock_Impact_%")
plt.show()
data_meta = data[data['Company'] == 'Meta']
print(data_meta)
print(" ")
plt.figure(figsize=(10,4))
plt.plot(data_meta['Date'],data_meta["Stock_Impact_%"], color='y')
plt.title("Change in Stock value of Meta")
plt.xlabel("Date ('Year')")
plt.ylabel("Stock_Impact_%")
plt.show()
data_google = data[data['Company'] == 'Google']
print(data_google)
print(" ")
plt.figure(figsize=(10,4))
plt.plot(data_google['Date'],data_google["Stock_Impact_%"], color='orange')
plt.title("Change in Stock value of Google")
plt.xlabel("Date ('Year')")
plt.ylabel("Stock_Impact_%")
plt.show()



#Events when Maximum stock Impact was observed
#check for OpenAI
print(data_Openai.sort_values(by='Stock_Impact_%', ascending=False))
#Check meta
print(data_meta.sort_values(by='Stock_Impact_%', ascending=False))

#check for google
print(data_google.sort_values(by='Stock_Impact_%', ascending=False))

#AI Revenue Growth of the companies
sns.scatterplot(x='Date', y= 'AI_Revenue_Growth_%', data = data, hue='Company')
plt.show()
data.sort_values(by=['AI_Revenue_Growth_%'])
#OpenAI's AI Revenue Growth year by year
plt.plot(data_Openai["Date"], data_Openai['AI_Revenue_Growth_%'], color ='m')
plt.show()
plt.plot(data_google["Date"], data_google['AI_Revenue_Growth_%'], color ='c')
plt.show()
plt.plot(data_meta["Date"], data_meta['AI_Revenue_Growth_%'], color ='black')
plt.show()

#NOTE SCATTER PLOT FOR GOOGLE AND META IS ALOMOST SAME AOVE RESEARCH IS DONE, DISCOVERED ALMOST SAME THATS WHY IT DISPLAYED SAME
#correlation between the columns

sns.heatmap(data.corr(numeric_only=True))
plt.show()
#Expendiure vs Revenue year by year
spend =data.groupby('Year')['R&D_Spending_USD_Mn'].sum()
print(spend)
plt.title("Combined R&D Spending Year-by-Year")
plt.xlabel("Year")
plt.ylabel("Amount in USD_$Mn")
#Showing the amount spend on R&D
plt.plot(spend.index,spend.values,color = 'r')
plt.show()

# Showing the Revenue earned 
revenue=data.groupby('Year')['AI_Revenue_USD_Mn'].sum()
print(revenue)
# Showing the Revenue earned 
plt.plot( revenue.index, revenue.values, color = 'g')

plt.title( "Combined Revenue Earned Year-by-Year")
plt.xlabel("Year")
plt.ylabel("Amount in USD_$Mn")
plt.show()
plt.plot(spend.index,spend.values,color = 'r')
plt.plot( revenue.index, revenue.values, color = 'g')
plt.title( "Combined Expenditure vs Revenue Earned Year-by-Year", fontsize=12)
plt.xlabel("Year")
plt.ylabel("Amount in USD_$Mn")
plt.legend(['Expenditure','Revenue'])
plt.show()


# Pairplot to show the relations between the columns

sns.pairplot(data);
plt.show()
#Event Impact Analysis
# Showing the various Events

data.Event.value_counts()
# Checking for a particular event

print(data[ data.Event == 'TensorFlow open-source release'])
tf=data.loc[3955 :3975]
print(tf)


# Showing the Impact with a line chart

plt.figure(figsize = (10,4))

plt.plot( tf['Date'], tf['Stock_Impact_%'], color = 'c')
plt.title("Comparison before and after the release of TensorFlow open-source")
plt.xlabel("Date")
plt.ylabel("Change in Stock %")

plt.show()

# Checking for a particular event

data[ data.Event == 'GPT-4 release']
gpt4 = data.loc[ 2984 : 3004]

print(gpt4)

# Showing the Impact with a line chart

plt.figure(figsize = (10,4))

plt.plot( gpt4['Date'], gpt4['Stock_Impact_%'], color = 'm')

plt.title("Comparison before and after the release of GPT-4")
plt.xlabel("Date")
plt.ylabel("Change in Stock %")

plt.show()
# Daily Average impact on the Stocks of the companies

print(data.groupby('Company')['Stock_Impact_%'].mean()*100)

# Daily Average Expenditure on R & D by the companies

print(data.groupby('Company')['R&D_Spending_USD_Mn'].mean())

# Maximum impact % on a company's stocks

print(data.groupby('Company')['Stock_Impact_%'].max())
#Change in the index wrt Year & Company

# Highest change in the index

stocks = data.groupby(['Year', 'Company'])['Stock_Impact_%'].max()

print(stocks)

stocks.plot(kind = 'barh', color = ['r', 'black', 'm'])

plt.title("change in index")

plt.show()
