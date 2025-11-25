# وظیفه: خواندن امن Excel با pandas
import pandas as pd

def load_excel(path, sheet=0):
    """
    Load a single Excel or CSV file into a DataFrame.
    """
    try:
        if path.lower().endswith(".csv"):
            return pd.read_csv(path)
        else:
            return pd.read_excel(path, sheet_name=sheet)
    except Exception as e:
        raise RuntimeError(f"Failed loading: {path}\n{e}")



def load_multiple(paths, sheet=0):
    """
    Load multiple Excel/CSV files and return a list of DataFrames.
    paths: list of file paths
    """
    dfs = []
    for p in paths:
        df = load_excel(p, sheet=sheet)  # ← استفاده مجدد از تابع اصلی
        dfs.append(df)
    return dfs