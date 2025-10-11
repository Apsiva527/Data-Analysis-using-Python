import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')
import datetime as dt
#pd.set.option('max_column')

#Prepare the data
df = pd.read_csv('C:/Users/amuda.sivaraj/PythonDatasets/mturkfitbit_export_3.12.16-4.11.16/Fitabase Data 3.12.16-4.11.16/dailyActivity_merged.csv')
df.shape  # It returns a tuple:(number_of_rows, number_of_columns)
df.columns
df.head(10)
df.dtypes
#clean the data, in this we noticed id in int change to str and date in object need to change date format
df['Id'] = df['Id'].astype(str)
df['ActivityDate'] = pd.to_datetime(df['ActivityDate'],format='%m/%d/%Y')
df.dtypes
#create new column distance difference =distance-tracker
df['distance_diff'] = df['TotalDistance'] - df['TrackerDistance']
df['distance_diff'].value_counts()
df.query('distance_diff > 0.0 ')
#simplicity sake changing the headers to lower case
df.columns = df.columns.str.lower()
df.columns
df.rename(columns ={'activitydate':'activity_date','totalsteps':'total_steps','totaldistance':'total_distance','trackerdistance':'tracker_distance',
       'loggedactivitiesdistance':'logged_activities_distance', 'veryactivedistance':'very_active_distance',
       'moderatelyactivedistance':'moderately_active_distance', 'lightactivedistance':'light_active_distance',
       'sedentaryactivedistance':'sedentary_active_distance', 'veryactiveminutes':'very_active_minutes', 'fairlyactiveminutes':'fairly_active_minute',
       'lightlyactiveminutes':'lightly_active_minutes', 'sedentaryminutes':'sedentary_minutes'},inplace = True)
df.columns
#Now create new columns to support the use case
day_of_week = df['activity_date'].dt.day_name()
df['day_of_week'] = day_of_week
df['n_day_of_week'] = df['activity_date'].dt.weekday #0 is Monday


df.columns
df.head(4)

#check null values, we can also use isnull()
df.isna().sum()

#check for duplicates
df.duplicated().sum()


# analysise phase: dividing them into different categories, so that we can get clear activities
#category 1
#Sedentary(lazy people):: less then 6000 steps on average
# active: between 6000 and 12000 on average
#very active: more than 12000 on average
id_grp = df.groupby(['id'])
id_avg_step = id_grp['total_steps'].mean().sort_values(ascending=False)
id_avg_step = id_avg_step.to_frame()
#to findout which categories each id belongs based on the steps provided, for that we need create condition

conditions = [
    (id_avg_step <= 6000),
    (id_avg_step > 6000) & (id_avg_step < 12000),
    (id_avg_step >= 12000)
]
values = ['sedentary','active', 'very_active']
#create header/column to hold the data
id_avg_step['activity_level'] =np.select(conditions, values, default='unknown')
id_activity_level = id_avg_step['activity_level']

df['activity_level'] = [id_activity_level[c] for c in df['id']]


#Pick data for analysis. create subset of data
df = df[['id', 'activity_date', 'total_steps', 'total_distance',
       'very_active_minutes', 'fairly_active_minute', 'lightly_active_minutes',
       'sedentary_minutes', 'calories', 'activity_level', 'day_of_week',
       'n_day_of_week']].copy()
print(df.head(3))
print(df['id'].value_counts())
print(df.describe())

#share
#correlation between steps and calries burned
ax = sns.scatterplot(x ='total_steps', y = 'calories', data=df, hue=df['activity_level'])
plt.title('Correlation calories vs steps')
plt.tight_layout()
plt.show()

#Average steps per day
day_of_week =['Monday','Tuesday','Wednesday', 'Thursday','Friday','Saturday','Sunday']
fig, ax = plt.subplots(1,1,figsize=(8,5))
day_grp = df.groupby(['day_of_week'])
avg_daily_steps = day_grp['total_steps'].mean()
avg_steps = df['total_steps'].mean()
plt.bar(avg_daily_steps.index, avg_daily_steps)
ax.set_xticks(range(len(day_of_week)))
ax.set_xticklabels(day_of_week)

ax.axhline(y=avg_daily_steps.mean(), color='blue',label = 'Avg daily steps')
ax.set_ylabel('Steps')
ax.set_xlabel('Day of Week')
ax.set_title('Avg number of steps per day')
plt.legend()
plt.show()


#percentage of activity in minutes
very_active_mins = df['very_active_minutes'].sum()
fairly_active_mins=df['fairly_active_minute'].sum()
lightly_active_mins=df['lightly_active_minutes'].sum()
sedentary_mins = df['sedentary_minutes'].sum()
slices = [very_active_mins,fairly_active_mins,lightly_active_mins,sedentary_mins]

labels = ['very_active_mins','fairly_active_mins','lightly_active_mins','sedentary_mins']
explode = [0,0,0,1]
plt.pie(slices, labels=labels, explode = explode,autopct ='%1.1f%%')
plt.title('%of activity level in minutes')
plt.show()

#correlation bewteen activity level in minutes and calories
n_day_of_week = [0,1,2,3,4,5,6]
fig, axes = plt.subplots(nrows=2, ncols=2,figsize=(8,9),dpi =70)
sns.scatterplot(data=df, x='calories', y = 'sedentary_minutes', hue ='activity_level', ax=axes[0,0],legend=False)
sns.scatterplot(data=df, x='calories', y = 'lightly_active_minutes', hue ='activity_level', ax=axes[0,1],legend=False)
sns.scatterplot(data=df, x='calories', y = 'fairly_active_minute', hue ='activity_level', ax=axes[1,0],legend=False)
sns.scatterplot(data=df, x='calories', y = 'very_active_minutes', hue ='activity_level', ax=axes[1,1],legend=True)

plt.legend(title = 'Activity Level',fontsize =18, bbox_to_anchor = (2.2,2.2))
fig.suptitle('Correlation Between activity level minutes and caloried', x=0.5,y=0.92, fontsize = 24)
plt.show()



