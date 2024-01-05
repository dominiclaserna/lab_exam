import pandas as pd

file_path = 'Exam_Table.csv'
data = pd.read_csv(file_path)

# Group by 'Scientific Name' and calculate the average estimated size
avg_size_by_name = data.groupby('Scientific Name')['Size Est (cm)'].mean().reset_index()

output_file_path = 'B4_output.csv'
avg_size_by_name.to_csv(output_file_path, index=False)

