from networkx import is_path
import pandas as pd 
import testdata

def read_data_xls_utility(file_path: str , sheet_name: str = None) -> list:
  """ 
  Reads data from an Excel file and returns a list of dictionaries.
"""
# Construct the full file path
full_path = f"testdata/login_data.xlsx"

# Read the Excel file
try:
    data_frame = pd.read_excel(full_path, sheet_name=sheet_name or 0)
    return data_frame.to_dict(orient='records')
except Exception as e:
    print(f"Error reading Excel file: {e}")
    return []

