import os

from src.utils.helper import (
    load_dataframe,
    save_dataframe
)
from src.utils.logger import Logger
from src.config.config import processed_data_path


def duplicate_handler(
    input_filename: str,
    output_filename: str
):

    Logger.info(
        f"Starting Duplicate Handler for {input_filename}"
    )

    input_path = os.path.join(
        processed_data_path,
        input_filename
    )

    df = load_dataframe(input_path)

    print("\nDataset Shape Before Handling Duplicate Values:")
    print(df.shape)

    duplicate_count = df.duplicated().sum()

    print("\nDuplicate Rows:")
    print(duplicate_count)

    df.drop_duplicates(inplace=True)

    print("\nShape After Handling Duplicate Values:")
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
        f"Duplicate-free dataset saved as {output_filename}"
    )

    print("\nDuplicate-free dataset saved successfully.")

    return df