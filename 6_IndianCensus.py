import pandas as pd
import jinja2
data = pd.read_csv(r"C:\Users\amuda\13DataAnalysisProject\Census+2011.csv")
print(data)

#how will you hide Index
    #data.style.hide_index()
#data.to_string(index=True)


#how can we set the caption/heading on the dataframe
data.style.set_caption('Indian Census 2011 Dataset')

#3. Show the records related with the districts-New Delhi, Lucknow, Jaipur.
#Syntax: df[df['col_name'].isin(['Item_1', 'Item_2', 'Item_3'])]
print(data[data['District_name'].isin(['New Delhi', 'Lucknow', 'Jaipur'])])


#4.Calculate state-Wise
#A.Total number of population
#B Total no of population with different religions
#sytanax: # df.groupby('Col_name_1').Col_names.sum()
print(data.groupby('State_name').Population.sum().sort_values(ascending=False))
#data.groupby('State_name').Population.sum().sort_values(ascending = False)

#data.groupby('State_name')['Hindus', 'Muslims', 'Christians', 'Sikhs', 'Buddhists', 'Jains'].sum().sort_values(by = 'Col_name')
print(data.columns)
print(data.groupby('State_name')[['Hindus', 'Muslims', 'Christians', 'Sikhs', 'Buddhists', 'Jains']].sum().sort_values(by = 'Hindus'))



#5 how many Male workers were there in Maharashtra state?

# df[df.Col_name_1 == 'Item']['Col_name_2'].sum()

print(data[data.State_name == 'MAHARASHTRA']['Male_Workers'].sum())


#6 how to set a column as Index of the dateframe
#df = df.set_index('Col_name')
data = data.set_index('District_code')
print(data)



#7a.Add a suffix to the column names,
# syntax: df = df.add_suffix('_value')
#print(data.add_suffix('_census'))

#7b.Add a Prefix to the column names
#syntax: df = df.add_prefix('value_')
print(data.add_prefix('census_'))
