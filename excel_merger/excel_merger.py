from excel_merger_toolkit.scanner import scan_excel_files
from excel_merger_toolkit.loader import load_excel
from excel_merger_toolkit.cleaner import clean_dataframe
from excel_merger_toolkit.merger import concat_dataframes
from excel_merger_toolkit.exporter import export_to_excel
import os

def main():
    base_dir = os.path.dirname(__file__)
    folder = os.path.join(base_dir, 'excel_merger_toolkit', 'files')

    print("🔍 Scanning folder...")
    paths = scan_excel_files(folder)

    all_dfs = []
    print("📥 Loading files...")

    for p in paths:
        df = load_excel(p)
        df = clean_dataframe(df)
        all_dfs.append(df)

    print("🔗 Merging...")
    merged = concat_dataframes(all_dfs)

    print("💾 Exporting...")
    
    outputPath = os.path.join(base_dir, 'excel_merger_toolkit', "output", "merged_output.xlsx")
    os.makedirs(os.path.dirname(outputPath), exist_ok=True)
    export_to_excel(merged, outputPath)

    print("✅ Done! File saved: merged_output.xlsx")

if __name__ == "__main__":
    main()