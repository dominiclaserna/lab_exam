import pandas as pd

file_path = 'Exam_Table.csv'
data = pd.read_csv(file_path)


pomacentrus_adelus_data = data[data['Scientific Name'] == 'Pomacentrus adelus']

average_count = pomacentrus_adelus_data['Count'].mean()

print(f"The average count for Pomacentrus adelus is: {average_count}")
