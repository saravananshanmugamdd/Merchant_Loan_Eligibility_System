import os

from src.utils.helper import (
    load_dataframe,
    save_dataframe
)
from src.config.config import processed_data_path
from src.utils.logger import Logger


def handle_null_values(
    input_filename: str,
    output_filename: str
):

    Logger.info(
        f"Starting Null Value Handler for {input_filename}"
    )

    input_path = os.path.join(
        processed_data_path,
        input_filename
    )

    df = load_dataframe(input_path)

    print("\nDataset Shape Before Handling Null Values:")
    print(df.shape)

    print("\nRemaining Null Values:")
    print(df.isnull().sum())

    columns_to_drop = [
        "brand",
        "brand:wikidata",
        "dispensing",
        "addr:street"
    ]

    existing_columns = [
        column
        for column in columns_to_drop
        if column in df.columns
    ]

    df.drop(
        columns=existing_columns,
        inplace=True
    )

    Logger.info(
        f"Removed {len(existing_columns)} high-null-value columns"
    )

    if "name" in df.columns:
        df["name"] = df["name"].fillna("Unknown")

    if "healthcare" in df.columns:
        df["healthcare"] = df["healthcare"].fillna("pharmacy")

    Logger.info("Remaining null values handled")

    print("\nRemaining Null Values After Processing:")
    print(df.isnull().sum())

    print("\nShape After Handling Null Values:")
    print(df.shape)

    output_path = os.path.join(
        processed_data_path,
        output_filename
    )

    save_dataframe(
        df,
        output_path
    )

    Logger.info(
        f"Null-handled dataset saved as {output_filename}"
    )

    print("\nNull-handled dataset saved successfully.")

    return df