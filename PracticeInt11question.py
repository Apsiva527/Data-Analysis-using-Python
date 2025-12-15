import pandas as pd

# Sample DataFrame (replace with your actual data)
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
        'salary': [70000, 90000, 60000, 100000, 80000, 95000, 75000]}
df = pd.DataFrame(data)

top_5_salaries = df['salary'].nlargest(n=5)
print(top_5_salaries)

#OR
top_5_salaries_df = df.sort_values(by='salary', ascending=False).head(5)
print(top_5_salaries_df)


