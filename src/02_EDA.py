# Step 2: Exploratory Data Analysis (EDA)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the dataset
df = pd.read_csv('product_sales.csv')

# Minor cleaning: fix sales_method typos
df['sales_method'] = df['sales_method'].replace({
    'em + call': 'Email + Call',
    'email': 'Email',
    'call': 'Call'
})

# Create an output folder for charts
output_folder = 'charts'
os.makedirs(output_folder, exist_ok=True)

# 2.1 Sales Method Distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='sales_method', order=df['sales_method'].value_counts().index)
plt.title('Distribution of Sales Methods Used')
plt.xlabel('Sales Method')
plt.ylabel('Number of Customers')
plt.tight_layout()
plt.savefig(f'{output_folder}/sales_method_distribution.png')
plt.close()

# 2.2 Revenue Distribution (excluding missing revenue)
plt.figure(figsize=(8, 5))
sns.histplot(data=df[df['revenue'].notnull()], x='revenue', bins=30, kde=True)
plt.title('Distribution of Revenue')
plt.xlabel('Revenue ($)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig(f'{output_folder}/revenue_distribution.png')
plt.close()

# 2.3 Revenue Trends over Time by Sales Method
plt.figure(figsize=(10, 6))
sns.lineplot(data=df[df['revenue'].notnull()], x='week', y='revenue', hue='sales_method', estimator='mean')
plt.title('Average Revenue over Weeks by Sales Method')
plt.xlabel('Week')
plt.ylabel('Average Revenue ($)')
plt.legend(title='Sales Method')
plt.tight_layout()
plt.savefig(f'{output_folder}/revenue_by_week_and_method.png')
plt.close()

print("✅ EDA charts created and saved successfully!")