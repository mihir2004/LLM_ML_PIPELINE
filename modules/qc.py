import pandas as pd
from pandas_profiling import ProfileReport

def run_qc_report(df):
    profile = ProfileReport(df, minimal=True)
    stats = {
        'columns': df.dtypes.astype(str).to_dict(),
        'missing_percent': (df.isna().mean() * 100).round(2).to_dict(),
        'outliers': {},
        'type_mismatches': {},
        'num_rows': len(df),
    }
    return stats
