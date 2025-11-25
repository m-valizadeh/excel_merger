# وظیفه: خروجی نهایی به Excel یا CSV
import pandas as pd

def export_to_excel(df, output_path):
    """Save the final merged file to Excel."""
    df.to_excel(output_path, index=False)


def export_to_csv(df, output_path):
    """Save the final merged file to CSV."""
    df.to_csv(output_path, index=False, encoding="utf-8")
