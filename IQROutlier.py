import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({
    "Sales": [100, 120, 130, 115, 140, 1000, 125, 135],
    "Profit": [10, 12, 14, 11, 13, 100, 15, 14]
})
print(df)
Original=df.copy()
#print(Original)

# Replace outliers on all numeric columns
def replace_outliers_IQR_multi(df):
    numeric_cols = df.select_dtypes(include='number').columns

    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        median = df[col].median()

        df[col] = np.where(
            (df[col] < lower) | (df[col] > upper),
            median,
            df[col]
        )
    return df

    df = replace_outliers_IQR_multi(df)
    print(df)

    # Visualize Before/After
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].boxplot(Original['Sales'])
axes[0].set_title("Before Outlier Treatment")
axes[1].boxplot(df['Sales'])
axes[1].set_title("After Outlier Treatment")
plt.show()

