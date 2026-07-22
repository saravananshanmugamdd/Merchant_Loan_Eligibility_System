import os
import joblib

from src.utils.logger import Logger
from src.utils.helper import save_dataframe, load_dataframe
from src.utils.exceptions import ModelTrainingError
from src.config.config import processed_data_path

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.calibration import CalibratedClassifierCV

def train_models():
    try:
        Logger.info("Starting Model Training Pipeline")

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

        models ={ 
            "logistic_regression":LogisticRegression(
                max_iter=1000,
                random_state=42
                ),
                
                "decision_tree":DecisionTreeClassifier(
                    random_state=42
                ),

                "random_forest":
                RandomForestClassifier(
                    n_estimators=100,
                    random_state=42
                ),

                "knn":
                    KNeighborsClassifier(
                        n_neighbors=5
                    ),

                "gaussian_nb":
                    GaussianNB(),

                "svm":CalibratedClassifierCV(SVC(
                    random_state=42),
                    ensemble=False)

        }

        model_directory = "models"

        os.makedirs(
            model_directory,
            exist_ok=True
        )

        trained_models= {}

        for model_name, model in models.items():

            Logger.info(f"Training {model_name} model")

            print(f"\n Training {model_name}")

            model.fit(
                x_train,
                y_train
            )

            trained_models[model_name]=model

            model_path = os.path.join(
                model_directory,
                f"{model_name}_model.pkl"
            )

            joblib.dump(
                model,
                model_path
            )

            print(f"\n {model_name}saved Succesfully")

            Logger.info(f"{model_name} training completed")

        print("===============Model Training Completed")

        return trained_models      
        
    except Exception as e:

        Logger.error(
            f"model training failed :{e}"
        )

        raise ModelTrainingError(
            "failed to train model"
        ) from e