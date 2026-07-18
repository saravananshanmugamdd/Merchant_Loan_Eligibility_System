import pandas as pd
import os

def save_dataframe(df:pd.DataFrame ,file_path:str):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    df.to_csv(file_path, index=False)

def load_dataframe(file_path):
    return pd.read_csv(file_path)
    



