import pandas as pd
df1=pd.DataFrame({"CustomerID":[1,2,3],"Name":["Jonhn","Sara","David"]})
df2=pd.DataFrame({"CustomerID":[2,3,4],"Sales":[300,500,150]})
#1. Basic Merge (INNER JOIN)
df_merged = pd.merge(df1, df2, on="CustomerID")
print(df_merged)

#2. Merge on Different Column Names
df_merged1 = pd.merge(df1, df2, left_on="CustomerID", right_on="CustomerID")
print(df_merged1)

#3. Left Join
df_left = pd.merge(df1, df2, on="CustomerID", how="left")
print(df_left)

#4. Right Join
df_right=pd.merge(df1,df2, on = "CustomerID", how="right")
print(df_right)

#5 Outer Join
df_outer = pd.merge(df1, df2, on="CustomerID", how="outer")
print(df_outer)

#🔹 6. Merge on Multiple Columns : Note: date column
#df_multi = pd.merge(df1, df2, on=["CustomerID", "Date"])
#print(df_multi)

#7. Add Suffixes to Avoid Duplicate Column Names
df_merge1 = pd.merge(df1, df2, on="CustomerID", suffixes=("_left", "_right"))
print(df_merge1)
