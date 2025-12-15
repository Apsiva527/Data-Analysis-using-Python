import pandas as pd
df = pd.DataFrame({
    "Department": ["IT", "IT", "HR", "HR", "Finance"],
    "Salary": [70000, 80000, 60000, 65000, 90000]
    })
df = df.assign(
    Gender=["M", "F", "F", "F", "M"],
    Bonus=[5000, 6000, 3000, 3500, 7000],
    Age=[29, 31, 26, 28, 35]
)

print(df)
#Basic GroupBy + Aggregate
df_groupbyBasic = df.groupby("Department")["Salary"].mean()
print(df_groupbyBasic)

#Multiple Aggregations
df_multigroupby=df.groupby("Department")["Salary"].agg(["mean", "max","min"])
print(df_multigroupby)
#Group by multiple columns
df_mutlicolgrp = df.groupby(["Department", "Gender"])["Salary"].sum()
print(df_mutlicolgrp)
#Aggregate multiple columns at once
df_aggmulticol =df.groupby("Department").agg({
    "Salary": "mean",
    "Bonus": "sum",
    "Age": "max"
})

print(df_aggmulticol)
#Rename aggregated columns
dfrenameaggcolname= df.groupby("Department")["Salary"].agg(
    AvgSalary = "mean", 
    MaxSalary ="max",
    MinSalary ="min")
print(dfrenameaggcolname)
#Reset index if you want a clean DataFrame
result = df.groupby("Department")["Salary"].mean().reset_index()
print(result)