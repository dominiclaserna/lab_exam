import pandas as pd

file_path = 'Exam_Table.csv'
data = pd.read_csv(file_path)

# Convert 'Replicate' column to string to handle float values
data['Replicate'] = data['Replicate'].astype(str)

# Replace any commas with dashes in the specified columns
columns_to_replace_comma = ['Location', 'Site', 'Replicate']
data[columns_to_replace_comma] = data[columns_to_replace_comma].replace(',', '-', regex=True)


data['HRID'] = data['Location'] + '-' + data['Site'] + '-' + data['Replicate']

# Insert 'HRID' column at the beginning of the DataFrame
data.insert(0, 'HRID', data.pop('HRID'))


output_file_path = 'B6_output.csv'
data.to_csv(output_file_path, index=False)

