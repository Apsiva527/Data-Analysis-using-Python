import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
sns.set_theme(style="whitegrid", palette="Set2")
data = pd.read_csv(r"C:\Users\amuda.sivaraj\PythonDatasets\13PythonDApractice\HR_Data_MNC_Data Science Lovers.csv")
print(data)

print(data.info())
# Removing unwamnted column from the dataframe

data.drop( 'Unnamed: 0', axis = 1, inplace = True)
print(data.info())
# Change the data-tpye of Date colum
data['Hire_Date'] = pd.to_datetime(data['Hire_Date'])
print(data.info())
print(data['Performance_Rating'].unique())
print(data['Performance_Rating'].value_counts())
print(data['Performance_Rating'].mean())
print(data['Experience_Years'].nunique())
print(data['Experience_Years'].unique())
sns.countplot(x='Experience_Years', data = data)
plt.show()
print(data['Experience_Years'].value_counts())

# Consider the columns having data-type 'Object' only
print(data.select_dtypes(include='object'))
print(data.select_dtypes( include = 'number'))

#1 what is the distribution of employee status(Active, Resigned, Retired, Terminated)?
status=data['Status'].value_counts()
print(type(status))
print(status)
status.plot(kind = 'pie',colors = 'mygr',autopct = '%1.1f%%',explode =(0.03,0.03,0.03,0.03))
plt.show()
#2 How many empoyees are there in each department?
data['Department'].value_counts()
sns.countplot(x='Department',data=data)
plt.show()
plt.figure(figsize=(10,5))
data['Job_Title'].value_counts()
sns.countplot(x='Job_Title',data=data)
plt.xticks(rotation='vertical')
plt.show()

#3 what is the average salary by department?
dept = data.groupby('Department')['Salary_INR'].mean()/1000
print(type(dept))
#draw graph salry vs dept
dept.plot(x=dept.index,y=dept.values,color ='c',kind='bar',legend= True, width = 0.3 )
plt.grid()
plt.title("Average Salary in Departments")
plt.ylabel("Salary")

plt.show()

#4 what is the distribution of work modes(on-site, Remote)?
work=data['Work_Mode'].value_counts()
work.plot(kind = 'pie',colors = 'cr',autopct = '%1.1f%%',shadow=True)
plt.show()

#5 which job title has the highest average salary?
salary=data.groupby('Job_Title')['Salary_INR'].mean()/1000
plt.figure(figsize=(10,5))
salary.plot(x=salary.index,y=salary.values,color ='g',kind='bar',legend= True, width = 0.3 )
plt.grid(True)
plt.title("Average Salary wrt Job Title")
plt.ylabel("Salary")
plt.show()
#6 what is the average salry in different department based on job title?
dept_job=data.groupby(['Department','Job_Title'])['Salary_INR'].mean()/1000
print(dept_job)

import random
num_bars = len(dept_job)
random_colors = [f'#{random.randint(0, 0xFFFFFF):06x}' for _ in range(num_bars)]

dept_job.plot( kind = 'barh', figsize = (10,5), color = random_colors)

plt.title('Average Salary in Different Departments')
plt.xlabel("Salary")

plt.savefig('new_chart.png', bbox_inches='tight')

plt.show()


#7 How many employees resigned & Terminated in each department?
print(data.Status.unique())
data_resigned=data[data['Status']=='Resigned']
r_emp=data_resigned.groupby('Department')['Status'].count()
plt.figure(figsize=(8,4))

r_emp.plot( x = r_emp.index, y = r_emp.values , kind = 'bar', color = 'black', legend = True, label = 'Resigned')

plt.title("No. of Resigned employees")
plt.ylabel("Count")

plt.show()
#Terminated
data_terminated=data[data['Status']=='Terminated']

print(data_terminated)
t_emp=data_terminated.groupby('Department')['Status'].count()

plt.figure(figsize=(10,6))
t_emp.plot(x=t_emp.index,y = t_emp.values,kind='bar',color='r', legend=True,label = 'Terminated')
plt.title("No. of Terminated employees")
plt.ylabel("Count")
plt.show()

#Both in same graph
plt.figure(figsize=(10,6))
r_emp.plot( x = r_emp.index, y = r_emp.values , kind = 'bar', color = 'black', legend = True, label = 'Resigned')
t_emp.plot(x=t_emp.index,y = t_emp.values,kind='bar',color='r', legend=True,label = 'Terminated')
plt.title("No.of Resigned & Terminated  employees")
plt.ylabel("Count")
plt.show()
#8 How does salary vary with year of experience
print(data['Experience_Years'].nunique())
print(data.groupby('Experience_Years')['Salary_INR'].mean())

#9 what is the average performance rating by department?
PR=data.groupby('Department')['Performance_Rating'].mean()
plt.figure(figsize=(10,6))
PR.plot( x = PR.index, y = PR.values , kind = 'bar', color = 'lightgreen')
plt.title("Average Performance Ratings Department Wise")
plt.ylabel("Rating")
plt.show()
#10 which country have the highest concentration of employess?
data['Country'] = data['Location'].apply(lambda x :str(x.split(',')[1]))
print(data)
print(data.Country.unique())
print(data.Country.nunique())
print(data.Country.value_counts())

#11 Is there a correlation between performance rating and salary?
print(data['Performance_Rating'].corr(data['Salary_INR']))

# Alternated Command to show Correlation
print(data[['Performance_Rating','Salary_INR']].corr())
sns.heatmap(data.corr(numeric_only=True))
plt.show()

#12 How has the number of hires changed overtime(per year)?
print(data.Hire_Date.dtype)
#Note we need to create new column year which we need to insert between column
pd.set_option('display.max_columns', None)
print(data.insert(5,'Year',data['Hire_Date'].dt.year))
print(data)
print(data.Year.unique())
print(data.Year.nunique())
hire=data.groupby('Year')['Employee_ID'].count()
print(hire)

#now draw grpah


plt.figure(figsize=(10,5))
hire.plot(x = hire.index, y = hire.values, kind = 'bar', color = 'violet')
plt.grid(True, color ='green')
plt.title("No. of Employees Hired in any Year")

plt.ylabel("Count")

plt.show()
#13 Compare salaries of Remote vs On-Site employees - is there a significant difference?
print(data.groupby('Work_Mode')['Salary_INR'].mean())
#14 Find the top 10 employees with the highest salary in each department
top_10=data.groupby('Department').apply(lambda x:x.nlargest(10,'Salary_INR'))
print(top_10)
print(top_10.head(40))
print(top_10.tail(30))
#15 Identify departments with the highest attrition rate(Resigned %)
dept_counts=data.groupby('Department')['Status'].agg(total_emp='count', resigned = lambda x:(x == 'Resigned').sum())
print(dept_counts)
type(dept_counts)
# Calculate attrition rate

dept_counts['attrition_rate_%'] = (dept_counts['resigned'] / dept_counts['total_emp']) * 100

# Sort by attrition rate (highest first)

dept_counts.sort_values("attrition_rate_%", ascending = False)

