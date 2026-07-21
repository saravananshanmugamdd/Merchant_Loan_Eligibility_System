import os 

from src.utils.logger import Logger
from src.utils.helper import save_dataframe, load_dataframe
from src.config.config import processed_data_path
from sklearn.model_selection import train_test_split

def prepare_ml_dataset():

    Logger.info("Started ML Dataset Preparation")

    input_path= os.path.join(
        processed_data_path,
        "chennai_pharmacies_target_engineered.csv"
    )

    df=load_dataframe(input_path)


    print("\n Dataset Shape")
    print(df.shape)

    feature_columns = [
    "nearby_hospital_count",
    "nearby_bank_count",
    "nearby_atm_count",
    "nearby_clinic_count",
    "nearby_supermarket_count",
    "nearby_bus_stop_count"
]
    target_column=["loan_eligibility_proxy"]

    x = df[feature_columns]

    y = df[target_column]

    x_train, x_test, y_train, y_test = train_test_split( x, y, test_size=0.2, random_state=42, stratify=y)

    print("\nTraining Data Shape:")
    print(x_train.shape)

    print("\nTesting Data Shape:")
    print(x_test.shape)

    train_df = x_train.copy()
    train_df[target_column] = y_train

    test_df = x_test.copy()
    test_df[target_column] = y_test

    train_output_path =  os.path.join(
        processed_data_path,
        "train.csv"
    )

    save_dataframe(
        train_df,
        train_output_path
    )

    test_output_path = os.path.join(
        processed_data_path,
        "test.csv"
    )

    save_dataframe(
        test_df,
        test_output_path
    )

    Logger.info(" ML Train and Test Dataset Saved Successfully ")

    print("\n ML Train and Test Dataset Saved Successfully")

    return(
        x_train,
        x_test,
        y_train,
        y_test
    )







