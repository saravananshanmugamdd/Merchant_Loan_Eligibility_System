import argparse

from src.collectors.osm_collector import collect_all_osm_data
from src.config.osm_config import OSM_COLLECTIONS
from src.preprocessing.coordinate_pipeline import coordinate_pipeline
from src.preprocessing.data_cleaning import clean_data
from src.preprocessing.null_value_handler import handle_null_values
from src.preprocessing.duplicate_handler import duplicate_handler
from src.preprocessing.datatype_handler import handle_datatypes
from src.feature_engineering.feature_pipeline import feature_pipeline
from src.feature_engineering.feature_validation import validate_feature
from src.target_engineering.target_creator import create_data
from src.modeling.data_split import prepare_ml_dataset

from src.modeling.train_model import train_models
from src.modeling.model_evaluation import evaluate_models
from src.modeling.prediction import MerchantLoanPrediction


def run_collection():

    print("\n========== DATA COLLECTION ==========")

    collect_all_osm_data()


def run_preprocessing():

    print("\n========== PREPROCESSING ==========")

    for collection in OSM_COLLECTIONS:

        print(
            f"\n========== PROCESSING "
            f"{collection['raw_file']} =========="
        )

        coordinate_pipeline(
            input_filename=collection["raw_file"],
            output_filename=collection["coordinate_file"]
        )

        clean_data(
            input_filename=collection["coordinate_file"],
            output_filename=collection["clean_file"]
        )

        handle_null_values(
            input_filename=collection["clean_file"],
            output_filename=collection["null_file"]
        )

        duplicate_handler(
            input_filename=collection["null_file"],
            output_filename=collection["duplicate_file"]
        )

        handle_datatypes(
            input_filename=collection["duplicate_file"],
            output_filename=collection["datatype_file"]
        )

    print(
        "\n========== ALL DATASETS PREPROCESSED SUCCESSFULLY =========="
    )

def run_feature_engineering():

    print("\n========== FEATURE ENGINEERING ==========")

    feature_pipeline()

def run_feature_validation():

    print("\n =============Feature Validation ==========")

    validate_feature()

def run_target_featuring():

    print("\n =============Target Engineering ============")

    create_data()

def run_ml_data_preparation():

    print("\n =============Preparing ML Dataset============")

    prepare_ml_dataset()

def run_model_training():

    print("\n==========Training Model================")

    train_models()

def run_model_evaluation():

    print("\n ===========Evaluating Model===========")

    evaluate_models()

def run_model_prediction():

    print("\n =========== Model Prediction ===========")


def main():

    parser = argparse.ArgumentParser(
        description="Merchant Loan Eligibility ML Pipeline"
    )

    parser.add_argument(
        "--stage",
        choices=[
            "collect",
            "preprocess",
            "features",
            "validate",
            "target",
            "prepare",
            "train",
            "evaluate",
            "predict",
            "all"
        ],
        default="all",
        help="Select pipeline stage to execute"
    )

    args = parser.parse_args()


    if args.stage == "collect":

        run_collection()


    elif args.stage == "preprocess":

        run_preprocessing()


    elif args.stage == "features":

        run_feature_engineering()


    elif args.stage == "validate":

        run_feature_validation()


    elif args.stage == "target":

        run_target_featuring()

    elif args.stage == "prepare":

        run_ml_data_preparation()

    elif args.stage == "train":

        run_model_training()

    elif args.stage =="evaluate":

        run_model_evaluation()

    elif args.stage =="predict":

        run_model_prediction()

    elif args.stage == "all":

        run_collection()

        run_preprocessing()

        run_feature_engineering()

        run_feature_validation()

        run_target_featuring()

        run_ml_data_preparation()

        run_model_training()

        run_model_evaluation()

        run_model_prediction()


if __name__ == "__main__":

    main()