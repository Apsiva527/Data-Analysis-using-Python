#This script reads a CSV file named data.csv with headers in the first row, creates a DataFrame, computes descriptive statistics for all columns (including object dtype) using describe(include='all'), and prints the result.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr

# Path to the CSV file. The first row is treated as headers by default (header=0).
#data_path = "C:\Users\amuda\Genrative AI for Data Analyst\laptop_pricing_dataset_mod2.csv"

# Read the CSV file into a DataFrame. Assumes the first row contains headers.
df = pd.read_csv(r"C:\Users\amuda\Genrative AI for Data Analyst\laptop_pricing_dataset_mod2.csv")
print(df.info())
# Generate descriptive statistics for all columns, including object (categorical) types.
description = df.describe(include="all")

# Output the description to stdout
print(description)
# 1) Regression plots: Price vs each numeric feature
regression_features = ['CPU_frequency', 'Screen_Size_inch', 'Weight_pounds']
for feature in regression_features:
    plt.figure(figsize=(6, 4))
    sns.regplot(x=feature, y='Price', data=df, scatter_kws={'alpha': 0.6})
    plt.title(f'Regression of Price on {feature}')
    plt.xlabel(feature)
    plt.ylabel('Price')
    plt.tight_layout()
    plt.savefig(f'regression_{feature}_vs_Price.png')
    plt.close()

# 2) Box plots: Price across categorical/numeric attributes
box_features = ['Category', 'GPU', 'OS', 'CPU_core', 'RAM_GB', 'Storage_GB_SSD']
for feature in box_features:
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=feature, y='Price', data=df)
    plt.title(f'Price distribution by {feature}')
    plt.xlabel(feature)
    plt.ylabel('Price')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'boxplot_{feature}_Price.png')
    plt.close()

    # Ensure the target column exists
if 'Price' not in df.columns:
    print("Error: 'Price' column not found in dataset.")
else:
    # Identify all numeric feature columns excluding the target 'Price'
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if 'Price' in numeric_cols:
        numeric_cols.remove('Price')

    results = []
    # Compute Pearson correlation and p-value for each numeric feature against Price
    for col in numeric_cols:
        subset = df[[col, 'Price']].dropna(subset=[col, 'Price'])
        if subset.shape[0] < 2:
            # Not enough data to compute correlation
            r = np.nan
            p = np.nan
        else:
            r, p = pearsonr(subset[col], subset['Price'])
        results.append({'Attribute': col, 'Pearson_r': r, 'p_value': p})

    # Present results as a single DataFrame
    summary_df = pd.DataFrame(results)
    print(summary_df)

    # Assumes a DataFrame named 'df' exists with columns: 'GPU', 'CPU_core', and 'Price'
# 1) Build a pivot table grouping by GPU (rows) and CPU_core (columns) and aggregating Price by mean
pivot_table = df.pivot_table(index='GPU', columns='CPU_core', values='Price', aggfunc='mean')

# 2) Plot a pcolor plot for the pivot table
plt.figure(figsize=(8, 6))
pc = plt.pcolor(pivot_table.values, cmap='viridis', shading='auto')
plt.colorbar(pc, label='Mean Price')
plt.xlabel('CPU_core')
plt.ylabel('GPU')
plt.xticks(np.arange(0.5, pivot_table.shape[1], 1), pivot_table.columns, rotation=45, ha='right')
plt.yticks(np.arange(0.5, pivot_table.shape[0], 1), pivot_table.index)
plt.title('Mean Price by GPU and CPU_core')
plt.tight_layout()
plt.savefig('pivot_pcolor_mean_price.png')
plt.close()

