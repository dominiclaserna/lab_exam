import pandas as pd
import random as random
# Read the CSV file
data= pd.read_csv("Exam_Table.csv")


data_transposed = data.T
data_transposed.to_csv("b6_output1.csv",index=False)