import os
import joblib
import pandas as pd

from src.utils.logger import Logger
from src.utils.exceptions import PredictionError


class MerchantLoanPrediction:

    def __init__(self):

        try:
            Logger.info("Loading Final Loan Eligibility Model")

            model_path = os.path.join(
                "models",
                "final_model.pkl"
            )

            if not os.path.exists(
                model_path
            ):

                raise FileNotFoundError(
                    f"Final model not found: {model_path}"
                )

            self.model = joblib.load(model_path)

            Logger.info("Final Model Loaded Successfully")

        except Exception as e:

            Logger.error(
                f"Failed to load final model: {e}"
            )

            raise PredictionError(
                "Failed to load final loan eligibility model."
            ) from e


    def predict(
        self,
        input_data
    ):

        try:

            Logger.info("Starting Loan Eligibility Prediction")

            input_df = pd.DataFrame([input_data])

            feature_columns = [
                "nearby_hospital_count",

                "nearby_bank_count",

                "nearby_atm_count",

                "nearby_clinic_count",

                "nearby_supermarket_count",

                "nearby_bus_stop_count"
            ]

            input_df = input_df[feature_columns]

            prediction = self.model.predict(input_df)

            if prediction[0] == 1:
                result = "Eligible"
            else:
                result = "Not Eligible"


            Logger.info(f"Prediction Completed: {result}")


            return result


        except Exception as e:

            Logger.error(f"Prediction Failed: {e}")

            raise PredictionError(
                "Failed to generate loan eligibility prediction."
                ) from e