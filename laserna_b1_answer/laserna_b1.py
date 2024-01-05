import pandas as pd

# Read the CSV file
file_path = 'Exam_Table.csv'
data = pd.read_csv(file_path)

# Filter rows where Interval is "30-0"
filtered_data = data[data['Interval'] == "30-0"]

# Save the filtered data to a new CSV file
output_file_path = 'B1_output.csv'
filtered_data.to_csv(output_file_path, index=False)


