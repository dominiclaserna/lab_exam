import pandas as pd
import random as random
# Read the CSV file
data= pd.read_csv("Exam_Table.csv")
data['HRID'] = range(1, len(data) + 1)
column_order = ['HRID']
data.iloc[:, -1] = data.iloc[:, 1].astype(str)  +"-"+data.iloc[:, 2].astype(str)+"-"+data.iloc[:, 6].astype(str)
data = data[column_order]
# View the first 5 rows
print(data)
# data.insert(2,"Random",[random.randint(0,1) for i in range (0,len(data))])
data.to_csv("b6_output1.csv",index=False)
# data_transposed.to_csv("b6_output1.csv",index=False)