import pandas as pd

# Extracting data using Pandas
df = pd.read_csv("C:\\path.csv) # For .xlsx use read_excel() instead
# Filtering dataframe
df = df[(df['Column_name']==value)]

# Slicing data frame in list
ids = df["Column_name"][:len].values
