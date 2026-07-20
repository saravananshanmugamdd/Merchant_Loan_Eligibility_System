from src.collectors.osm_collector import collect_osm_data
from src.config.osm_config import PLACE,OSM_COLLECTIONS
from src.preprocessing.coordinate_pipeline import coordinate_pipeline
from src.preprocessing.data_cleaning import clean_data
from src.preprocessing.null_value_handler import handle_null_values
from src.preprocessing.duplicate_handler import duplicate_handler
from src.preprocessing.datatype_handler import handle_datatypes
from src.feature_engineering.feature_pipeline import feature_pipeline

def main():

    for config in OSM_COLLECTIONS:

        collect_osm_data(
            place=PLACE,
            tag_key=config["tag_key"],
            tag_value=config["tag_value"],
            filename=config["raw_file"]
        )

        coordinate_pipeline(
            input_filename=config["raw_file"],
            output_filename=config["coordinate_file"]
        )

        clean_data(
            input_filename=config["coordinate_file"],
            output_filename=config["clean_file"]
        )

        handle_null_values(
            input_filename=config["clean_file"],
            output_filename=config["null_file"]
        )

        duplicate_handler(
            input_filename=config["null_file"],
            output_filename=config["duplicate_file"]
        )

        handle_datatypes(
            input_filename=config["duplicate_file"],
            output_filename=config["datatype_file"]
        )

        feature_pipeline()

if __name__ == "__main__":
    main()