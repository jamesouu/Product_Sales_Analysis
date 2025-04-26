import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv('product_sales.csv')

# Step 2: Basic structure information
print("Dataset Info:")
print(df.info())

# Step 3: Preview first few rows
print("\nFirst 5 Rows:")
print(df.head())

# Step 4: Check missing values in each column
print("\nMissing Values:")
print(df.isnull().sum())

# Step 5: Check unique values for categorical columns
print("\nUnique values in 'sales_method':")
print(df['sales_method'].unique())

print("\nUnique values in 'state':")
print(df['state'].unique())

# Step 6: Summary statistics for numerical columns
print("\nSummary Statistics:")
print(df.describe())