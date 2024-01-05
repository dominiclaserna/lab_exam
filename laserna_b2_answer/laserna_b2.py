import pandas as pd

file_path = 'Exam_Table.csv'
data = pd.read_csv(file_path)

filtered_data = data[data['Genus'].str.lower().str.startswith('st', na=False)]

output_file_path = 'B2_output.csv'
filtered_data.to_csv(output_file_path, index=False)


