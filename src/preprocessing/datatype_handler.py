import os

import pandas as pd

from src.utils.logger import Logger
from src.utils.helper import load_dataframe, save_dataframe
from src.config.config import processed_data_path



def handle_datatypes():

    Logger.info("Starting Datatype Handler Pipeline")


    input_path = os.path.join(
        processed_data_path,
        "chennai_pharmacies_null_handled.csv"
        )

    df = load_dataframe(input_path)

    print("\nCurrent Datatypes:")
    print(df.dtypes)

    Logger.info("Datatype conversion started")


    # String columns
    string_columns = [
        "geometry",
        "amenity",
        "healthcare",
        "name"
        ]


    for col in string_columns:
        df[col] = df[col].astype("string")


    numerical_columns = [
        "longitude",
        "latitude"
        ]

    for col in numerical_columns:
        df[col] = pd.to_numeric(df[col])

    Logger.info("Datatype conversion completed")

    expected_columns = {

        "geometry":"string",
        "amenity":"string",
        "healthcare":"string",
        "name":"string",
        "longitude":"float64",
        "latitude":"float64"

    }


    for column, dtype in expected_columns.items():

        if str(df[column].dtype) != dtype:

            Logger.error(
                f"{column} datatype mismatch"
            )
            raise TypeError(
                f"{column} datatype should be {dtype}"
            )

    Logger.info("Datatype validation successful")

    print("\nValidated Datatypes:")
    print(df.dtypes)

    output_path = os.path.join(
        processed_data_path,
        "chennai_pharmacies_datatype_processed.csv"
    )


    save_dataframe(
        df,
        output_path
        )


    Logger.info("Datatype processed dataset saved successfully")
    return df