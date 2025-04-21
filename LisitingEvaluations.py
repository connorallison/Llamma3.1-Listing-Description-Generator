import pandas as pd
import numpy as np

def read_last_columns_csv(file_path, num_columns=4):
    """
    Reads a CSV file and returns the last 'num_columns' columns as a NumPy matrix.

    Args:
        file_path (str): The path to the CSV file.
        num_columns (int): The number of last columns to read (default: 4).

    Returns:
        numpy.ndarray: A NumPy matrix containing the data from the last 'num_columns' columns,
                       or None if an error occurs.
    """
    try:
      df = pd.read_csv(file_path)
      if num_columns > len(df.columns):
        raise ValueError(f"The CSV file has fewer than {num_columns} columns.")
      
      matrix = df.iloc[:, -num_columns:].values
      return matrix
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{file_path}' is empty.")
        return None
    except ValueError as e:
        print(f"ValueError: {e}")
        return None
    
# Example usage:
file_path = '/Users/connorallison/Library/CloudStorage/OneDrive-Personal/Desktop/School/MSDA/Spring 2025/Deep Learning/LLM Project/CA-Copy of 50 Listing Annotations - Sheet1.csv'
matrix_data1 = read_last_columns_csv(file_path)
file_path2 = '/Users/connorallison/Library/CloudStorage/OneDrive-Personal/Desktop/School/MSDA/Spring 2025/Deep Learning/LLM Project/rankings Joel - Sheet1.csv'
matrix_data2 = read_last_columns_csv(file_path2)
file_path3 = '/Users/connorallison/Library/CloudStorage/OneDrive-Personal/Desktop/School/MSDA/Spring 2025/Deep Learning/LLM Project/N Copy of 50 Listing Annotations - Sheet1.csv'
matrix_data3 = read_last_columns_csv(file_path3)

combined_matrix = (matrix_data1 + matrix_data2 + matrix_data3)/3

combined_matrix = np.round(combined_matrix, decimals=2)
# Convert to DataFrame (optionally with column names)
df = pd.DataFrame(combined_matrix, columns=['Human-Like', 'Engagement', 'Uniqueness', 'Impression'])
df.round(2)
# Write to CSV
df.to_csv('/Users/connorallison/Library/CloudStorage/OneDrive-Personal/Desktop/School/MSDA/Spring 2025/Deep Learning/LLM Project/evaluation_array.csv', index=False)
