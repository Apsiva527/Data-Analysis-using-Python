import pandas as pd

# Create a simple dictionary of data
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)