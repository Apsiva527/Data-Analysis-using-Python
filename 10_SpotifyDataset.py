import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#%matplotlib inline
data = pd.read_csv(r"C:\Users\amuda.sivaraj\PythonDatasets\13PythonDApractice\Spotify_Youtube.csv")
print(data)
print(data.columns)
print(data.info())
pd.set_option('display.max_columns', None)
# removing the unwanted columns from the dataframe 
print(data.drop(columns = ['Unnamed: 0', 'Url_spotify', 'Uri', 'Url_youtube'], inplace = True))
print(data)
# checking missing values counts in each column of the dataframe
print(data.isna().sum())

# filling the missing values with 0 in Likes & Commnets column
data['Likes'] = data['Likes'].fillna(0)
data['Comments'] = data['Comments'].fillna(0)

data.isnull().sum()  # to check the count of missing values in each column
data.dropna(inplace = True) 
print(data.isnull().sum())     # to check the count of missing values in each column
print(data.info())
#1: Top 10 Artists - with the highest views on Youtube?
Artist_grouped = data.groupby('Artist')['Views'].sum()
Artist_sorted = Artist_grouped.sort_values(ascending=False) #need to display in descending(highest to lowest)
print(Artist_sorted)

#Q2 Top 10 Tracks- with the highest streams on spoptify?
x = data[['Track', 'Stream']]  # creating a new dataframe with 2 columns - Track & Stream
print(x)
most_stream_track = x.sort_values(['Stream'],ascending = False).head(10) # sorting the dataframe wrt Stream column
print(most_stream_track)
#Q2A: 5 tracks with lowest stream on spotify?
y = data[['Track', 'Stream']]
print(y)
lowest_stream = y.sort_values(['Stream'],ascending=True).head(5)
print(lowest_stream)
#Q3, what are the most common Album Types on spotify? How many tracks belong to each album type?
print(data.Album_type.unique())
a_type= data['Album_type'].value_counts()
print(a_type)

# draw a Pie chart, gives clear picture of tracks belong to each alubum type
plt.pie(a_type, labels = a_type.index, autopct="‘%1.1f%%’", startangle=60,colors='myr', shadow='True', explode= (0.05,0.05,0.05),pctdistance=0.75)
plt.show()

#Q4: How do the average views, likes and comments are compared between different Alubum types?
# group the Album Type column, and show the mean of three columns
df = data.groupby('Album_type')[['Likes','Views', 'Comments']].mean()

print(type(df))
print(df.reset_index())

# melt - unpivot a dataframe
#pd.melt(frame, id_vars=None, value_vars=None, var_name=None, value_name='value')
#df.columns = df.columns.str.strip()  # removes extra spaces
print(df.columns)
"""
df_melted  = pd.melt( df, id_vars = 'Album_type', var_name = "Attribute", value_name = 'Total' )
print(df_melted)
# Draw the Bar Plot

plt.figure(figsize = (9,4))

sns.barplot( x = 'Album_type', y = 'Total', hue = 'Attribute', data = df_melted );
"""
#Q5: Top 5 Youtube channel- based on the views?
c_views = data.groupby('Channel')['Views'].sum().sort_values(ascending=False).head()

c_views
c_views = c_views.reset_index()

c_views.head(10)
type(c_views)

# sns.set_style("whitegrid")

sns.barplot( x = "Views", y = "Channel", data = c_views, color='black')
plt.title('Top 5 Channels by Views')
plt.xlabel('Views')
plt.ylabel('Channel')
plt.show()

#Q6: Top most track - based on the view?
print(data.sort_values( by = 'Views', ascending = False).head(1))

#Q7: Which top 7 tracks have the highest Like-to_view ratio on youtube?
track_lv = data[['Track', 'Likes', 'Views']]
track_lv['LV_Ratio'] = data['Likes']/data['Views'] * 100
print(track_lv)

print(track_lv.sort_values( by = 'LV_Ratio', ascending = False).head(7))

#Q7A: Which top 3 tracks have the lowest Like-to_view ratio on youtube?
print(track_lv.sort_values( by = 'LV_Ratio', ascending = True).head(3))
#Q8: Top Albums having the Tracks with maximum danceablity

# creating groups for each Album

T_danceability =  data.groupby('Album')['Danceability'].sum().sort_values(ascending=False)

T_danceability
data[data.Album == 'Greatest Hits']          # filtering the dataframe with 'Greatest Hits'

#9: what is correlation between views, Likes, comments and Stream?
# creating a new dataframe with 4 columns

df_vlcs = data[['Views', 'Likes', 'Comments', 'Stream']] 

df_vlcs

df_vlcs.corr()                      # correlation matrix for the required columns
sns.heatmap(df_vlcs.corr())            # drawing a heatmap for the correlation matrix
plt.show()