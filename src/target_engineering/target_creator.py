import os

from src.utils.logger import Logger
from src.config.config import processed_data_path
from src.utils.helper import save_dataframe, load_dataframe

def create_data():

    Logger.info(
        "Starting Target Engineering Pipeline"
    )

    input_path=os.path.join(
        processed_data_path,
        "chennai_pharmacies_feature_engineered.csv"
    )

    df=load_dataframe(input_path)

    print("\n Dataset Shape")
    print(df.shape)

    df["Business_viability_score"]=(

        df["nearby_hospital_count"] * 0.20
        + df["nearby_bank_count"] * 0.15
        + df["nearby_atm_count"] * 0.15
        + df["nearby_clinic_count"] * 0.15
        + df["nearby_supermarket_count"] * 0.15
        + df["nearby_bus_stop_count"] * 0.15
    )

    print("Business Viability Summary")

    print(df["Business_viability_score"].describe())

    threshold=(df["Business_viability_score"].median())

    df["loan_eligibility_proxy"] = (
        df["Business_viability_score"] >= threshold).astype(int)
    
    print("\nTarget Distribution:")

    print(df["loan_eligibility_proxy"].value_counts())

    print("\nTarget Percentage:")

    print(df["loan_eligibility_proxy"]
        .value_counts(normalize=True) * 100)
    
    output_path = os.path.join(
        processed_data_path,
        "chennai_pharmacies_target_engineered.csv"
    )

    save_dataframe(
        df,
        output_path
    )

    Logger.info("Target Engineering Pipeline Completed")


    print("\nTarget engineered dataset saved successfully.")

    print("\nFinal Dataset Shape:")

    print(df.shape)


    return df

