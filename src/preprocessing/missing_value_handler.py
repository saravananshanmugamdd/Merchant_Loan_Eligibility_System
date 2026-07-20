import os
import pandas as pd
from src.utils.logger import Logger

def calculate_missing_report(df):

    Logger.info("calculating missing value report")

    missing_percentage=(df.isnull().sum()/len(df))*100

    missing_report=pd.DataFrame({
        "columns"         :df.columns,
        "missing_values"  :df.isnull().sum(),
        "missing_percentage":missing_percentage.round(2)
    })

    missing_report=missing_report.sort_values(
        by="missing_percentage",
        ascending=False
    )

    return missing_report

def remove_high_missing_columns(df, threshold=90):
    Logger.info(f"Removing columns with more than {threshold}% missing values")

    missing_report=calculate_missing_report(df)

    columns_to_drop=missing_report[missing_report["missing_percentage"]>threshold]["columns"].to_list()

    print("\n columns to drop")

    print(columns_to_drop)

    df=df.drop(columns=columns_to_drop)

    Logger.info(f"{len(columns_to_drop)} columns removed")

    return df

def validate_missing_values(df):

    Logger.info("validating remaining missing values")

    print("\n remaining missing values")

    print(df.isnull().sum())