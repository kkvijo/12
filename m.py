import pandas as pd

# Sample data
data = {
    'feature1': [1, 2, 3, 4, 5],
    'feature2': [2, 3, 4, 5, 6],
    'target': ['A', 'A', 'B', 'B', 'B']  # Assuming classification labels
}

# Create DataFrame
df = pd.DataFrame(data)

# Print the DataFrame
print(df)
