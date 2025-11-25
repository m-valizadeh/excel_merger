# Excel Merger Toolkit

### Overview

A Python utility for scanning, loading, cleaning, merging, and exporting Excel/CSV files from a target directory.
Main entry point: `excel_merger.py`

### Project Structure

General_utils/
│
├── excel_merger.py
└── excel_merger_toolkit/
    ├── __init__.py
    ├── scanner.py      # Detects Excel/CSV files
    ├── loader.py       # Loads selected sheets
    ├── cleaner.py      # Cleans and normalizes data
    ├── merger.py       # Merges all DataFrames
    ├── exporter.py     # Exports final merged file
    └── files/          # Input folder for Excel/CSV files

### Installation

Make sure Python ≥ 3.10 is installed.

Run:

```bash
pip install -r requirements.txt
```

### Usage

```bash
cd "C:\MHD\Python_Progs"
python -m General_utils.excel_merger
```

Output file: merged_YYYYMMDD_HHMMSS.xlsx

### Notes

- Supports `.xlsx`, `.xls`, `.csv`
- Handles multiple sheets
- Cleans and merges using Pandas

### Author

Mohammadreza Valizadeh
Industrial Controller & Python Developer
