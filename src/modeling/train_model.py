import os
import joblib

from src.utils.logger import Logger
from src.utils.helper import save_dataframe, load_dataframe
from src.utils.exceptions import ModelTrainingError
from src.config.config import processed_data_path

from sklearn.linear_model import LogisticRegression

def train_logistic_regression():
    try:
        Logger.info("Started Logistic Regression Model Training")

        train_path = os.path.join(
            processed_data_path,
            "train.csv"
        )

        train_df = load_dataframe(train_path)

        print("\n Train Dataset Shape")
        print(train_df.shape)

        target_column = ("loan_eligibility_proxy")

        x_train = train_df.drop(columns= [target_column])
        y_train = train_df[target_column]

        model = LogisticRegression(
            max_iter=1000,
            random_state=42
        )

        Logger.info("Training Logistic regression Model")

        model.fit(x_train, y_train)

        Logger.info(" Logistic Regression Model Training Completed")

        model_directory = "models"

        os.makedirs(
            model_directory,
            exist_ok=True
        )

        model_path = os.path.join(
            model_directory,
            "logistic_regression_model.pkl"
        )

        joblib.dump(
            model,
            model_path
        )

        print("\n Logistic Regression Model"
              "saved Succesfully"
             )
        print(f"Model path = {model_path}")

        Logger.info(
            f"Logistic Regression Model "
            f"saved at {model_path}"
            )        
        
    except Exception as e:

        Logger.error(
            "Logistic Regression Training Failed"
            f"{str(e)}"
        )

        raise ModelTrainingError(
            "failed to train Logistic Regression model"
        ) from e