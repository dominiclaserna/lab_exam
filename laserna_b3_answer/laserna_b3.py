import pandas as pd
import random as random
# Read the CSV file
data= pd.read_csv("Exam_Table.csv")

# data['ID'] = range(1, len(data) + 1)


# column_order = ['ID'] + [col for col in data.columns if col != 'ID']
# data.iloc[:, 1] = 'META-' + data.iloc[:, 1].astype(str)
# data = data[column_order]
data=data.iloc[:, 10]
# data=[i for i in data if i=='30-0']
data=pd.unique(data)

f = open("B1_output", "w")
f.write(str(data))
f.close()
# View the first 5 rows

# data.insert(2,"Random",[random.randint(0,1) for i in range (0,len(data))])
# data_transposed = data.T
# print(data_transposed.head())
# data_transposed.to_csv("table1.csv",index=False)


