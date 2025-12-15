import pandas as pd

# Step 1: Read the CSV file into a DataFrame
#file_path = "C:\Users\amuda\Genrative AI for Data Analyst\2016.csv"  # Replace with the actual path to your CSV file
df = pd.read_csv(r"C:\Users\amuda\Genrative AI for Data Analyst\2016.csv", header=0)  # header=0 uses the first row as column names

# Step 2: Print the first 5 rows of the DataFrame
print(df.head())

#Write a python code that performs the following tasks:
#1. Check the data types of the columns and see if it correct
print("Column Data Types:")
print(df.dtypes)
print(df.info())