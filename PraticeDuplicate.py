import pandas as pd

data = {
    "Customer": ["John", "Sara", "David", "John", "Emma", "Sara"],
    "Product":  ["Laptop", "Mouse", "Desk", "Laptop", "Chair", "Mouse"],
    "Sales":    [900, 75, 200, 900, 180, 75]
}

df = pd.DataFrame(data)

# Find duplicates in Customer + Product
#

df_duplicate=df[df.duplicated(["Customer", "Product"], keep=False)]
print(df_duplicate)
df_removeduplicate=df.drop_duplicates()
print(df_removeduplicate)