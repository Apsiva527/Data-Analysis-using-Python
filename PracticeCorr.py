#12 th question
# Create a sample DataFrame
import pandas as pd
data = {
    'ColumnA': [10, 12, 15, 18, 20],
    'ColumnB': [5, 6, 7, 9, 10],
    'ColumnC': [2, 4, 3, 5, 6],
    'ColumnD': [1, 2, 1, 3, 2]
}
df = pd.DataFrame(data)

# Calculate the correlation matrix
correlation_matrix = df.corr()
print(correlation_matrix)

# Calculate the correlation between 'ColumnA' and 'ColumnB'
correlation_ab = df['ColumnA'].corr(df['ColumnB'])
print(f"Correlation between ColumnA and ColumnB: {correlation_ab}")
#Basic Example
df = pd.DataFrame({
    "Sales": [200, 220, 250, 270, 300],
    "Profit": [20, 25, 30, 35, 40],
    "Expenses": [150, 160, 170, 180, 190]
})

Basiccorr=df.corr()
print(Basiccorr)
import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.show()
