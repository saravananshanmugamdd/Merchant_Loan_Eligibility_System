import os
import joblib
import pandas as pd

from sklearn.metrics import accuracy_score, recall_score, f1_score, precision_score, confusion_matrix, classification_report

from src.utils.logger import Logger
from src.utils.helper import save_dataframe, load_dataframe
from src.utils.exceptions import PredictionError
from src.config.config import processed_data_path

def evaluate_models():

    try:

        Logger.info("starting Model Evaluation")

        test_path = os.path.join(
            processed_data_path,
            "test.csv"
        )

        test_df = load_dataframe(test_path)

        print("\n Test Dataset Shape")
        print(test_df.shape)

        target_column = ("loan_eligibility_proxy")

        x_test = test_df.drop(columns= [target_column])
        y_test = test_df[target_column]

        model_directory = "models"
        
        model_names = [

            "logistic_regression",
            "decision_tree",
            "random_forest",
            "knn",
            "gaussian_nb",
            "svm"]
        
        results = []

        
        for model_name in model_names:

            Logger.info(f"Evaluating {model_name} model")


            print(f"\nEvaluating: {model_name}")

            model_path = os.path.join(
                model_directory,
                f"{model_name}_model.pkl"
            )

            model = joblib.load(model_path)

            if not os.path.exists(model_path):
                raise FileNotFoundError(
                    f"model not found : {model_path}"
                )
            
            model = joblib.load(model_path)

            Logger.info("Loaded  Model")

            y_pred = model.predict(x_test)

            accuracy = accuracy_score(
                y_test,
                y_pred,
            )

            precision = precision_score(
                y_test,
                y_pred,
                zero_division=0
            )

            f1 = f1_score(
                y_test,
                y_pred,
                zero_division=0
            )

            recall = recall_score(
                y_test,
                y_pred,
                zero_division=0
            )

            results.append({

                "model": model_name,

                "accuracy": round(
                    accuracy,
                    4
                ),

                "precision": round(
                    precision,
                    4
                ),

                "recall": round(
                    recall,
                    4
                ),

                "f1_score": round(
                    f1,
                    4
                )})
            
        results_df = pd.DataFrame(results)

        results_df = results_df.sort_values(
            by="f1_score",
            ascending=False
        )

        print("\n =========== Model evaluation score ==========")
        
        print(results_df.to_string(index=False))

        output_path = os.path.join(
            processed_data_path,
            "model_comparison.csv"
        )

        save_dataframe(
            results_df,
            output_path
        )

        best_model = results_df.iloc[0]


        print(
            "\n========== BEST MODEL =========="
        )

        print(
            f"Model     : {best_model['model']}"
        )

        print(
            f"Accuracy  : {best_model['accuracy']}"
        )

        print(
            f"Precision : {best_model['precision']}"
        )

        print(
            f"Recall    : {best_model['recall']}"
        )

        print(
            f"F1 Score  : {best_model['f1_score']}"
        )


        Logger.info(
            "Model Evaluation Pipeline Completed"
        )


        return results_df


    except Exception as e:

        Logger.error(
            f"Model Evaluation Failed: {e}"
        )

        print(f"\nActual Error: {e}")

        raise PredictionError(
            "Failed to evaluate machine learning models."
        ) from e


