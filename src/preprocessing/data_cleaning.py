import os
import pandas as pd
from src.utils.logger import Logger
from src.utils.helper import save_dataframe, load_dataframe
from src.config.config import raw_data_path, processed_data_path

def clean_pharmacy_data():
    Logger.info("pharmacies data cleaning initialised")

    input_path=os.path.join(
        raw_data_path,
        "chennai_pharmacies.csv"
    )
    df=load_dataframe(input_path)

    print(df.shape)
    print(df.columns)
    print(df.head())
    print(df.isnull().sum())
        
    
