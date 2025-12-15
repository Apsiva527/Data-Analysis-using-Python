import pandas as pd

data = {'date_col': ['2023-01-15', '2023-02-20', '2023-03-25']}
df = pd.DataFrame(data)

df['date_col'] = pd.to_datetime(df['date_col'])
print(df.dtypes)