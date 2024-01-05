import pandas as pd

file_path = 'Exam_Table.csv'
data = pd.read_csv(file_path)

unique_scientific_names = data['Scientific Name'].unique()

# Create a DataFrame with unique scientific names
unique_scientific_names_df = pd.DataFrame({'Unique Scientific Names': unique_scientific_names})


output_file_path = 'B3_output.csv'
unique_scientific_names_df.to_csv(output_file_path, index=False)

