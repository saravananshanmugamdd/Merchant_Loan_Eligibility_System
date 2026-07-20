from src.collectors.osm_collector import collect_pharmacies
from src.preprocessing.coordinate_pipeline import coordinate_pipeline
from src.preprocessing.data_cleaning import clean_pharmacy_data
from src.preprocessing.null_value_handler import handle_null_values
from src.preprocessing.duplicate_handler import duplicate_handler
from src.preprocessing.datatype_handler import handle_datatypes

def main():

    collect_pharmacies()
    coordinate_pipeline()
    clean_pharmacy_data()
    handle_null_values()
    duplicate_handler()
    handle_datatypes()


if __name__ == "__main__":
    main()