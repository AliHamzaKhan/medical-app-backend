import pandas as pd
from typing import List, Dict, Any

def read_excel_data(
    file_path: str,
    sheet_name: str = None,
    to_json: bool = False
) -> List[Dict[str, Any]]:
    """
    Reads data from an Excel file and returns it as a list of dictionaries.

    Args:
        file_path (str): The path to the Excel file.
        sheet_name (str, optional): The name of the sheet to read. 
                                      If None, reads the first sheet. Defaults to None.
        to_json (bool, optional): Whether to convert the data to a JSON string. 
                                 Defaults to False.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries representing the rows of the Excel sheet.
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        if to_json:
            return df.to_json(orient='records')
        return df.to_dict(orient='records')
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
