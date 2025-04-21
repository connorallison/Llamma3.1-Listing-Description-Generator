from LisitingEvaluations import read_last_columns_csv 
import numpy as np
import pandas as pd

file_path = '/Users/connorallison/Library/CloudStorage/OneDrive-Personal/Desktop/School/MSDA/Spring 2025/Deep Learning/LLM Project/TestSet2 Rankings Connor - Sheet1.csv'
matrix_data1 = read_last_columns_csv(file_path)
file_path2 = '/Users/connorallison/Library/CloudStorage/OneDrive-Personal/Desktop/School/MSDA/Spring 2025/Deep Learning/LLM Project/TestSet2 Rankings Joel - Sheet1.csv'
matrix_data2 = read_last_columns_csv(file_path2)
file_path3 = '/Users/connorallison/Library/CloudStorage/OneDrive-Personal/Desktop/School/MSDA/Spring 2025/Deep Learning/LLM Project/TestSet2 Rankings Nick - Sheet1.csv'
matrix_data3 = read_last_columns_csv(file_path3)

combined_matrix = (matrix_data1 + matrix_data2 + matrix_data3)/3

combined_matrix = np.round(combined_matrix, decimals=2)
# Convert to DataFrame (optionally with column names)
df = pd.DataFrame(combined_matrix, columns=['Human-Like', 'Engagement', 'Uniqueness', 'Impression'])
df.round(2)
# Write to CSV
df.to_csv('/Users/connorallison/Library/CloudStorage/OneDrive-Personal/Desktop/School/MSDA/Spring 2025/Deep Learning/LLM Project/evaluation_array2.csv', index=False)
