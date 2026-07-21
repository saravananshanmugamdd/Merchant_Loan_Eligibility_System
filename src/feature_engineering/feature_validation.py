import os

from src.utils.logger import Logger
from src.utils.helper import load_dataframe
from src.config.config import processed_data_path

def validate_feature():

    Logger.info("Started Feature Validation ")

    input_path=os.path.join(
        processed_data_path,
        "chennai_pharmacies_feature_engineered.csv"
    )

    df=load_dataframe(input_path)

    feature_columns=[
        "nearby_hospital_count",
        "nearby_bank_count",
        "nearby_atm_count",
        "nearby_clinic_count",
        "nearby_supermarket_count",
        "nearby_bus_stop_count"
    ]

    print("\n========== FEATURE SUMMARY ==========")

    print(df[feature_columns].describe())


    print("\n========== NULL VALUES ==========")

    print(df[feature_columns].isnull().sum())

    print("\n========== ZERO VALUES ==========")

    print((df[feature_columns] == 0).sum())

    Logger.info("Feature Validation Completed")

    return df
