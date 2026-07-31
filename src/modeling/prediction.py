import os
import joblib
import pandas as pd

from src.utils.logger import Logger
from src.utils.exceptions import PredictionError
from src.utils.helper import save_dataframe, load_dataframe
from src.config.config import processed_data_path
from src.feature_engineering.neaby_counter import count_nearby_places
from src.feature_engineering.feature_pipeline import generate_nearby_features


class MerchantLoanPrediction:

    def __init__(self):

        try:
            Logger.info("Loading Final Loan Eligibility Model")

            model_path = os.path.join(
                "models",
                "final_model.pkl"
            )

            if not os.path.exists(model_path):
                raise FileNotFoundError(
                    f"Final model not found: {model_path}"
                )
            
        
            self.model = joblib.load(model_path)

            self.hospital_df =load_dataframe( os.path.join(
                processed_data_path,
                "chennai_hospitals_datatype_processed.csv"
            ))

            self.clinic_df = load_dataframe(os.path.join(
                processed_data_path,
                "chennai_clinics_datatype_processed.csv"
            ))

            self.bank_df = load_dataframe(os.path.join(
                processed_data_path,
                "chennai_banks_datatype_processed.csv"
            ))

            self.bus_stop_df = load_dataframe(os.path.join(
                processed_data_path,
                "chennai_bus_stops_datatype_processed.csv"
            ))

            self.atm_df =load_dataframe( os.path.join(
                processed_data_path,
                "chennai_atms_datatype_processed.csv"
            ))

            self.supermarket_df = load_dataframe(os.path.join(
                processed_data_path,
                "chennai_supermarkets_datatype_processed.csv"
            ))

            self.pharmacy_df =load_dataframe( os.path.join(
                processed_data_path,
                "chennai_pharmacies_datatype_processed.csv"
            ))

            Logger.info("Final Model and OSM datasets Loaded Successfully")

        except Exception as e:

            Logger.error(
                f"Failed to load final model: {e}"
            )

            raise PredictionError(
                "Failed to load final loan eligibility model."
            ) from e
    


    def predict(
        self,
        latitude,
        longitude
    ):

        try:

            Logger.info(
                "Starting Loan Eligibility Prediction"
            )

            input_df = pd.DataFrame([{
                "latitude": latitude,
                "longitude": longitude,
            }])

            input_df = generate_nearby_features(
                source_df=input_df,
                hospital_df=self.hospital_df,
                clinic_df=self.clinic_df,
                bank_df=self.bank_df,
                atm_df=self.atm_df,
                supermarket_df=self.supermarket_df,
                bus_stop_df=self.bus_stop_df
            )

            feature_columns = [

                "nearby_hospital_count",

                "nearby_bank_count",

                "nearby_atm_count",

                "nearby_clinic_count",

                "nearby_supermarket_count",

                "nearby_bus_stop_count"

            ]

            model_input = input_df[
                feature_columns
            ]

            print(
                f"\nGenerated Features:\n"
                f"{model_input}"
            )

            prediction = self.model.predict(
                model_input
            )

            if prediction[0] == 1:

                result = "Eligible"

            else:

                result = "Not Eligible"


            features = model_input.iloc[0].to_dict()


            Logger.info(
                f"Prediction Completed: {result}"
            )


            return {
                "prediction": result,
                "features": features
            }


        except Exception as e:

            Logger.error(
                f"Prediction Failed: {e}"
            )

            raise PredictionError(
                "Failed to generate loan eligibility prediction."
            ) from e