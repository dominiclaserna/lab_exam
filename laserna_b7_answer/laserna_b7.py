import pandas as pd

file_path = 'Exam_Table.csv'
data = pd.read_csv(file_path)

# Transpose the DataFrame
transposed_data = data.T

# Save the transposed data to a new CSV file
output_file_path = 'B7_output.csv'
transposed_data.to_csv(output_file_path, header=False)
