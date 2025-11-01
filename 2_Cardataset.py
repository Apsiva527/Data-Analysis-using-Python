import pandas as pd
cardataset = pd.read_csv(r"C:\Users\amuda\13DataAnalysisProject\Project+2+-+Cars+Dataset.csv")
print(cardataset)
#1.Instruction for data cleaning
#Find all null value in dataset and replace with mean with the mean of that column
print(cardataset.isnull().sum())
print(cardataset['Cylinders'].fillna(cardataset['Cylinders'].mean(), inplace = True))

#2.Question(Based on Values Counts)
#Check what are the different types of make are there in our dataset. And what is the count(occurance) of each Make in the data?
print(cardataset['Make'].value_counts())


#3.Instruction(Filtering)
#Show all the records where Origin is Asia or Europe
print(cardataset.head(2))
#print(cardataset[(cardataset['Origin'] == 'Asia') | (cardataset['Origin'] == 'Europe')])

print(cardataset[cardataset['Origin'].isin(['Asia' , 'Europe'])])
#4. Instruction(Removing unwanted records)
#Remove all the records(rows) where weight is above 4000
print(cardataset[~(cardataset['Weight'] > 4000)])



#5 Instruction (Applying function on a column)
#Increase all the values of 'MPG_City column by 3
print(cardataset.head(2))
print(cardataset['MPG_City'].apply(lambda x:x+3))




