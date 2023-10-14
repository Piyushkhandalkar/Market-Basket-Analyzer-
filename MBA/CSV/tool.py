import pandas as pd
import numpy as np

# Define the number of transactions and items
num_transactions = 9559  # Adjust as needed
num_items = 183  # Adjust as needed

# Generate random transaction data
data = np.random.choice(['Yes', 'No'], size=(num_transactions, num_items))

# Create a DataFrame
df = pd.DataFrame(data, columns=[f'Item{i+1}' for i in range(num_items)])

# Save the DataFrame to a CSV file
df.to_csv('large_dataset.csv', index=False)

print(f"CSV file 'large_dataset.csv' with {num_transactions} transactions and {num_items} items has been created.")

