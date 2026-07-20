import os
import pandas as pd

from src.utils.helper import save_dataframe, load_dataframe
from src.utils.logger import Logger
from src.config.config import processed_data_path

def duplicate_handler():

    Logger.info("started handling duplicate values")

    input_path=os.path.join(
        processed_data_path,
        "chennai_pharmacies_null_handled.csv"
    )

    df=load_dataframe(input_path)

    print("\n Dataset shape before handling duplicate values")
    print(df.shape)

    duplicate_count=df.duplicated().sum()

    print("\n Duplicate Rows ")
    print(duplicate_count)

    df.drop_duplicates(inplace=True)

    print("\n shape after handling duplicate values")
    print(df.shape)

    output_path=os.path.join(
        processed_data_path,
        "chennai_pharmacies_duplicate_removed.csv"
    )

    Logger.info("Duplicate Handler completed")

    print("\nDuplicate-free dataset saved successfully.")

    print("======Data Type check===========")

    print("\n Current Datatypes")
    print(df.dtypes)

    print("\n Datatype Information")
    print(df.info())