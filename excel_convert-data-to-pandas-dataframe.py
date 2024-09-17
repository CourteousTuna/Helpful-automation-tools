import pandas as pd

file_path = 'file.csv'

# Extracting data using Pandas
df = pd.read_csv(file_path) # For .xlsx use read_excel() instead

# Converts to string and removes last 4 characters
df['id_demande'] = df['id_demande'].astype(str).str[:-4]

# Slicing data frame in list
ids = df['id_demande'][:len].values

# Filtering df
df = df[df['type_demande'] == "PREST ADH"]
filtered_df = df[df['type_document_detaille'].isin(["FACTURE", "BULLETIN HOSPI VERST IJ"])]

# Group by unique combinations of id_demande and type_document_detaille 
df_grouped = filtered_df.groupby('id_demande')['type_document_detaille'].nunique()

# Counts the total number of rows with distinct id_demande
total_distinct_ids =  df[df['type_document_detaille'] == "FACTURE"]['id_demande'].nunique()

# Filter df by rows that have 2 rows with the same id_demande and distinct type_document_detaille values 
df_with_both = df_grouped[df_grouped == 2].index.tolist()

# Average number of lines per id_demande
lines_per_id = df.groupby('id_demande').size()
average_lines_per_id = lines_per_id.mean()


print(f"Total number of distinct id_demande: {total_distinct_ids}")
print(f"Number of id_demande that have both 'FACTURE' and 'BULLETIN HOSPI VERST IJ': {len(df_with_both)}")
print(f"Percentage of cases with both types: {(len(df_with_both) / total_distinct_ids) * 100:.2f}%")
print("\nFirst 20 id_demande that have both 'FACTURE' and 'BULLETIN HOSPI VERST IJ':")
print(df_with_both[:20]) # Display the first 20 id_demande that have both types
