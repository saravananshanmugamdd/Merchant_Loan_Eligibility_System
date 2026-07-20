import os
from src.utils.logger import Logger
from src.utils.helper import load_dataframe, save_dataframe
from src.config.config import processed_data_path
from src.preprocessing.missing_value_handler import calculate_missing_report,remove_high_missing_columns,validate_missing_values



def clean_data(
    input_filename: str,
    output_filename: str
):

    Logger.info(f"Starting Data Cleaning Pipeline{input_filename}")

    input_path = os.path.join(
    processed_data_path,
    input_filename
    )

    df = load_dataframe(input_path)

    print("Original Shape:", df.shape)

    report = calculate_missing_report(df)

    print(report)

    df = remove_high_missing_columns(
        df,
        threshold=90
    )

    validate_missing_values(df)

    print("\nShape After Cleaning:")
    print(df.shape)

    output_path = os.path.join(
        processed_data_path,
        output_filename
    )

    save_dataframe(
        df,
        output_path
    )

    Logger.info("Clean dataset saved successfully.")

    return df