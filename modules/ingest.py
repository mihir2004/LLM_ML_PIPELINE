import pandas as pd
from sqlalchemy import create_engine

def load_csv(file_obj):
    df = pd.read_csv(file_obj)
    return df

def load_db(uri):
    engine = create_engine(uri)
    df = pd.read_sql_table('public.your_table', engine)
    return df
