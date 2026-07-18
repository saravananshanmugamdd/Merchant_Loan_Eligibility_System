import osmnx as ox
import pandas as pd
import os

from src.utils.logger import Logger
from src.utils.helper import save_dataframe
from src.config.config import raw_data_path

def collector_pharmacies():
    Logger.info("starting pharmacy data collection")

    place="Chennai, Tamil Nadu, India"

    tags={
        "amenity": "pharmacy"
    }

    gdf=ox.features_from_place(place, tags)

    Logger.info(f"{len(gdf)} pharmacies downloaded")

    print(gdf.head())

    output_path=os.path.join(
        raw_data_path, 
        "chennai_pharmacies.csv"
    )

    save_dataframe(gdf, output_path)

    Logger.info("CSV saved successfully")

    print("completed")


