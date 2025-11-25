


import os

def scan_excel_files(folder_path, extensions=None):
 
    if extensions is None:
        extensions = [".xlsx", ".xls", ".csv"]

    files = []
    for fname in os.listdir(folder_path):
        if any(fname.lower().endswith(ext) for ext in extensions):
            files.append(os.path.join(folder_path, fname))

    return files
   
    # Scan a folder and return a list of Excel file paths.
    # Default extensions: xlsx, xls, csv
    # → وظیفه: پیدا کردن فایل‌های اکسل داخل یک پوشه
    