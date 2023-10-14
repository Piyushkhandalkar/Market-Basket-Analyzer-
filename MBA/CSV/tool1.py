import pandas as pd
import numpy as np
import random

# Define the number of transactions and items
num_transactions = 1000  # Adjust as needed
num_items = 20  # Adjust as needed

# Create a list of unique item names (e.g., 'Item1', 'Item2', ..., 'Item20')
item_names = [f'Item{i}' for i in range(1, num_items + 1)]

# Generate synthetic transaction data with fluctuating item combinations
transactions = []
for _ in range(num_transactions):
    # Create a transaction with a random number of items (varying from 1 to num_items)
    num_items_in_transaction = np.random.randint(1, num_items + 1)
    transaction = random.sample(item_names, num_items_in_transaction)
    transactions.append(transaction)

# Create a DataFrame from the transactions
df = pd.DataFrame(transactions, columns=[f'Item{i}' for i in range(1, num_items + 1)])

# Generate random support values for each item
min_support = 0.01  # Adjust as needed
max_support = 0.5   # Adjust as needed

# Randomly assign support values to each item
for item in df.columns:
    df[item] = np.random.uniform(min_support, max_support, num_transactions)

# Save the DataFrame to a CSV file
df.to_csv('association_rule_data.csv', index=False)

print(f'CSV file "association_rule_data.csv" with {num_transactions} transactions and {num_items} items has been created.')
