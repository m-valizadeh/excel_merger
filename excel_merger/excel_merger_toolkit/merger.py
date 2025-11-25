# وظیفه: ادغام چند فایل با روش‌های مختلف (concat / full outer merge / inner merge)
import pandas as pd

def concat_dataframes(df_list):
    """Simple vertical concatenation."""
    return pd.concat(df_list, ignore_index=True)


def merge_on_columns(df_list, on_columns, how="inner"):
    """
    Merge multiple DataFrames on specified columns.
    how: inner, outer, left, right
    """
    if not df_list:
        return None

    merged = df_list[0]

    for df in df_list[1:]:
        merged = merged.merge(df, on=on_columns, how=how)

    return merged
