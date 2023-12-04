import pandas as pd
import random as random
# Read the CSV file
data= pd.read_csv("Exam_Table.csv")
data['Pomacentrus adelus'] = range(1, len(data) + 1)
column_order = ['Pomacentrus adelus']
data.iloc[:, -1] = data.iloc[:, 10] 
data=data.iloc[:, 10].astype(str)+" " +data.iloc[:, 11].astype(str) 
f = open("B5_output", "w")

for i in data:
	if 'Pomacentrus adelus' in i:
		f.write(str(i))
		f.write("\n")
f.close()
# # data.insert(2,"Random",[random.randint(0,1) for i in range (0,len(data))])
# data.to_csv("b6_output1.csv",index=False)
# # data_transposed.to_csv("b6_output1.csv",index=False)