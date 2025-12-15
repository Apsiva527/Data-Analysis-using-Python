import pandas as pd
df = pd.read_csv(r'C:\Users\amuda\Data-Analysis-using-Python\sales_data.csv')
print(df)

# 1. Filter rows where Sales > 200
df_high_sales= df[df['Sales'] > 200]
print(df_high_sales)

# 2. Filter Electronics category
df_category=df[df['Category'] =='Electronics']
print(df_category)

# 3. Filter North region AND Sales > 300
df_north_Region = df[(df['Region'] == 'North') & (df['Sales'] >= 300)]
print(df_north_Region)

# 4. Filter rows where Quantity is between 2 and 10
df_quantity=df[df['Quantity'].between(2,10)]
print(df_quantity)

# 5. Filter rows based on date
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df_feb_orders = df[df["OrderDate"].between("02-01-2024", "02-29-2024")]
print(df_feb_orders)

#print(df)

#Multiple values df[col].isin([...]): This can be used when need OR condition
df_filtered_OR=df[df['Region'].isin(['North','West'])]
print(df_filtered_OR)

#2. Filter multiple Products
df_products=df[df['Product'].isin(['Laptop','Monitor'])]
print(df_products)

#3. Filter multiple Categories
df_catogories=df[df['Category'].isin(['Electronics','Furniture'])]
print(df_catogories)
#4. Filter multiple OrderIDs
df_orderIDS=df[df['OrderID'].isin([1002,1008])]
print(df_orderIDS)
#5. Using isin() with NOT condition
df_filter_NOTcondition= df[~df['Region'].isin(['North','West'])]
print(df_filter_NOTcondition)
#6. Filtering numeric values0
df_quanities=df[df['Quantity'].isin([2, 4, 10, 20])]
print(df_quanities)

#c.	Using .loc[] for Row and Column Selection     here ":" means retrive column  1. Select Rows by Label + All Columns
df_loc=df.loc[df['Region']=='North',:]
print(df_loc)
#2. Select Specific Columns for Filtered Rows
df_elec = df.loc[df["Category"] == "Electronics", ["OrderID", "Product", "Sales"]]
print(df_elec)
#3. Select Specific Rows by Index
df_index=df.loc[0]          # Row at index 0
df_index1=df.loc[0:3]        # Rows 0 to 3 (inclusive)
print(df_index)
print(df_index1)
#4. Select Specific Columns Only

df_speficcol=df.loc[:,['UnitPrice']]
print(df_speficcol)

#5. Select Rows AND Columns Together
df_rowCol=df.loc[df["Sales"] > 200, ["Customer", "Sales"]]
print(df_rowCol)

#6. Update Values Using .loc[]

#Example: Increase Sales by 10% for Electronics items
df_update=df.loc[df["Category"] == "Electronics", "Sales"] * 1.10
print(df_update)

#7. Select rows by date range using .loc[]
df_feb1 = df.loc[(df["OrderDate"] >= "2024-02-01") &
                (df["OrderDate"] <= "2024-02-29"),
                :]
print(df_feb1)

#e.	Filtering by String Patterns
#1. Filter rows where a column contains a substring
# Select rows where Customer name contains "John"
df_contains = df[df["Customer"].str.contains("John")]
print(df_contains)
#2. Filter rows where a string starts with a pattern
df_starts = df[df["Customer"].str.startswith("S")]
print(df_starts)
#3. Filter rows where a string ends with a pattern
df_ends = df[df["Customer"].str.endswith("Kim")]
print(df_ends)
#4. Filter rows using regex (pattern matching)
# Customers whose name starts with J or S
df_regex = df[df["Customer"].str.match("^[JS]")]
print(df_regex)
#5. Filter ignoring case
df_filterignore=df[df["Product"].str.contains("laptop", case=False)]
print(df_filterignore)
#f.	Using .query():

#1. Basic Filter
df_Basic=df.query("Sales > 200")
print(df_Basic)
#2. Multiple Conditions (AND / OR)
#AND condition
df_queryAnd=df.query("Sales > 200 and Category == 'Electronics'")
print(df_queryAnd)
#OR condition
df_Query_OR=df.query("Region == 'North' or Region == 'East'")
print(df_Query_OR)
#3. Using Variables in .query()
min_sales = 100
region_name = "West"

df_variables=df.query("Sales > @min_sales and Region == @region_name")
print(df_variables)

#4. Filter by String Patterns
#Note: Use engine='python' for string methods like .str.contains().
df_pattern=df.query("Customer.str.contains('John')", engine='python')
print(df_pattern)
#5. Filter by Date Range
df_dateRange= df.query("OrderDate >= '2024-02-01' and OrderDate <= '2024-02-29'")
print(df_dateRange)
#6. Filter Using isin() with .query()
df_query_isin =df.query("Region in ['North','South']")
print(df_query_isin)