# وظیفه: پاک‌سازی ستون‌ها، نرمال‌سازی، حذف فضای اضافی
def normalize_columns(df):
    """
    Remove whitespace and unify column names.
    """
    df.columns = [col.strip().replace("\n", " ").replace("  ", " ") for col in df.columns]
    return df


def clean_dataframe(df):
    """
    Clean full dataframe (strip spaces, normalize text).
    """
    df = normalize_columns(df)
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    return df
