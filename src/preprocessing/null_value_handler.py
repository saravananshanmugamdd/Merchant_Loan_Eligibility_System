import os
import pandas as pd

from src.utils.helper import save_dataframe, load_dataframe
from src.config.config import processed_data_path
from src.utils.logger import Logger

def handle_null_values():

    Logger.info("starting to handle null values")

    input_path=os.path.join(
        processed_data_path,
        "chennai_pharmacies_clean.csv"
    )

    df=load_dataframe(input_path)

    print("\n dataset shape before handling null values")
    print(df.shape)

    print("\n Remaining null values")
    print(df.isnull().sum())

    columns_to_drop=[
        "brand",
        "brand:wikidata",
        "dispensing",
        "addr:street"
    ]

    existing_columns=[column for column in columns_to_drop if column in df.columns]

    df.drop(columns=existing_columns, inplace=True)

    Logger.info("removed high null value columns")

    if "name" in df.columns:
        df["name"] = df["name"].fillna("Unknown")

    if "healthcare" in df.columns:
        df["healthcare"] = df["healthcare"].fillna("pharmacy")

    Logger.info("Remaining null values handled.")

    print("\nRemaining Null Values After Processing:")
    print(df.isnull().sum())

    print("\n shape after handling null values")
    print(df.shape)

    output_path=os.path.join(
        processed_data_path,
        "chennai_pharmacies_null_handled.csv"
    )

    save_dataframe(
        df, output_path
    )

    Logger.info("Null values handling completed")

    print("\nNull-handled dataset saved successfully.")