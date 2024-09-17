import pandas as pd

'''
This was used in a context where I had chunks of data concatenated horizontally in Excel,
 and I wanted to convert it to one chunk of data per line instead of multiple chunks of data on the same line. 

Additionally, the number of chunks of data varies on each line. 
'''

input_file = "file.xlsx"
output_file = "file.csv"

# Engine for xlsx
df = pd.read_excel(input_file, engine='openpyxl')

# Decode strings in the dataframe to proper Unicode 
# -> Avoid wrong conversions of é, è, à etc.
def force_unicode(value):
    if isinstance(value, str):
        return value.encode('utf-8').decode('utf-8', 'ignore')
    return value

# Apply to every cell in the dataframe
df = df.applymap(force_unicode)

# Writing to csv file
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    # Write the header of the output
    csvfile.write(",".join(['DocId'] + [f'Column_{i+1}' for i in range(10)]) + "\n")
    
    # Iterate the dataframe
    for index, row in df.iterrows():
        doc_id = row[0] 

        # Starting from column P, read chunks of 10 columns until a blank line is found
        start_col = 15 
        while start_col < len(row):
            line = row[start_col:start_col + 10]
            
            if line.isnull().all():
                break
            
            # Convert the line to a list and replace na values with ''
            line_values = line.fillna('').tolist()
            
            # Write the line to the CSV file
            csvfile.write(f"{doc_id}," + ",".join(map(str, line_values)) + "\n")
            
            start_col += 10
