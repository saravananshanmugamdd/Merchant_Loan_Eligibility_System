import os

from src.utils.logger import Logger
from src.utils.helper import save_dataframe, load_dataframe
from src.config.config import processed_data_path
from src.feature_engineering.neaby_counter import count_nearby_places


def generate_nearby_features(
    source_df,
    hospital_df,
    clinic_df,
    bank_df,
    atm_df,
    supermarket_df,
    bus_stop_df
):

    Logger.info("Generating Nearby Location Features")

    source_df = source_df.copy()

    source_df["nearby_hospital_count"] = count_nearby_places(
        source_df=source_df,
        target_df=hospital_df,
        radius=500
    )

    source_df["nearby_clinic_count"] = count_nearby_places(
        source_df=source_df,
        target_df=clinic_df,
        radius=500
    )

    source_df["nearby_bank_count"] = count_nearby_places(
        source_df=source_df,
        target_df=bank_df,
        radius=500
    )

    source_df["nearby_atm_count"] = count_nearby_places(
        source_df=source_df,
        target_df=atm_df,
        radius=500
    )

    source_df["nearby_supermarket_count"] = count_nearby_places(
        source_df=source_df,
        target_df=supermarket_df,
        radius=500
    )

    source_df["nearby_bus_stop_count"] = count_nearby_places(
        source_df=source_df,
        target_df=bus_stop_df,
        radius=500
    )

    Logger.info("Nearby Location Features Generated Successfully")

    return source_df


def feature_pipeline():

    Logger.info("Starting Feature Engineering Pipeline")

    pharmacy_path = os.path.join(
        processed_data_path,
        "chennai_pharmacies_datatype_processed.csv"
    )

    pharmacy_df = load_dataframe(pharmacy_path)

    print("\n Dataset Shape")

    print(pharmacy_df.shape)


    hospital_df = load_dataframe(
        os.path.join(
            processed_data_path,
            "chennai_hospitals_datatype_processed.csv"
        )
    )


    clinic_df = load_dataframe(
        os.path.join(
            processed_data_path,
            "chennai_clinics_datatype_processed.csv"
        )
    )


    bank_df = load_dataframe(
        os.path.join(
            processed_data_path,
            "chennai_banks_datatype_processed.csv"
        )
    )


    bus_stop_df = load_dataframe(
        os.path.join(
            processed_data_path,
            "chennai_bus_stops_datatype_processed.csv"
        )
    )


    atm_df = load_dataframe(
        os.path.join(
            processed_data_path,
            "chennai_atms_datatype_processed.csv"
        )
    )


    supermarket_df = load_dataframe(
        os.path.join(
            processed_data_path,
            "chennai_supermarkets_datatype_processed.csv"
        )
    )


    Logger.info("All OSM Datasets loaded successfully")


    pharmacy_df = generate_nearby_features(
        source_df=pharmacy_df,
        hospital_df=hospital_df,
        clinic_df=clinic_df,
        bank_df=bank_df,
        atm_df=atm_df,
        supermarket_df=supermarket_df,
        bus_stop_df=bus_stop_df
    )


    print("\n Feature Preview")

    print(
        pharmacy_df[
            [
                "name",
                "nearby_hospital_count",
                "nearby_bank_count",
                "nearby_atm_count",
                "nearby_clinic_count",
                "nearby_supermarket_count",
                "nearby_bus_stop_count"
            ]
        ].head()
    )


    output_path = os.path.join(
        processed_data_path,
        "chennai_pharmacies_feature_engineered.csv"
        )


    save_dataframe(
        pharmacy_df,
        output_path
    )


    Logger.info("Feature engineering pipeline completed")


    print("\nFeature engineered dataset saved successfully.")


    print("\nFinal Dataset Shape:")


    print(pharmacy_df.shape)


    return pharmacy_df