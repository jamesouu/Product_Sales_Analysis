# Step 3: Key Metric Definition - Average Revenue per Customer (ARPC)

import pandas as pd

# Load the dataset
df = pd.read_csv('product_sales.csv')

# Minor cleaning: fix sales_method typos if needed
df['sales_method'] = df['sales_method'].replace({
    'em + call': 'Email + Call',
    'email': 'Email',
    'call': 'Call'
})

# Step 3.1: Exclude rows with missing revenue
valid_revenue_df = df[df['revenue'].notnull()]

# Step 3.2: Calculate Total Revenue
total_revenue = valid_revenue_df['revenue'].sum()

# Step 3.3: Calculate Number of Customers
number_of_customers = valid_revenue_df['customer_id'].nunique()

# Step 3.4: Calculate Average Revenue per Customer (ARPC)
ARPC = total_revenue / number_of_customers

# Step 3.5: Display Result
print(f"✅ Average Revenue per Customer (ARPC): ${ARPC:.2f}")

############
############

# Group by sales_method
grouped = valid_revenue_df.groupby('sales_method')

# Calculate ARPC for each sales method
arpc_by_method = grouped.apply(lambda x: x['revenue'].sum() / x['customer_id'].nunique())

# Display results
print("✅ Average Revenue per Customer by Sales Method:")
print(arpc_by_method)