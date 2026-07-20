import os
from src.utils.logger import Logger
from src.utils.helper import save_dataframe, load_dataframe
from src.config.config import processed_data_path
from src.feature_engineering.neaby_counter import count_nearby_places

def feature_pipeline():

    Logger.info("Starting Feature Engineering Pipeline")

    input_path=os.path.join(
        processed_data_path,
        "chennai_pharmacies_datatype_processed.csv"
    )
    df=load_dataframe(input_path)

    print("\n Dataset Shape")
    print(df.shape)

    print(df[["name", "latitude", "longitude"]].head())

    Logger.info("Generating nearby pharmacy count")

    df["nearby_pharmacy_count"]= count_nearby_places(
        source_df=df,
        target_df=df,
        radius=500
    )

    print("\n Feature Preview")
    print(df[["name", "nearby_pharmacy_count"]].head())

    output_path = os.path.join(
        processed_data_path,
        "chennai_pharmacies_feature_engineered.csv"
    )

    save_dataframe(
        df,
        output_path
    )

    Logger.info("Feature engineering completed")

    print("\nFeature engineered dataset saved successfully.")