import os
import osmnx as ox

from src.utils.logger import Logger
from src.utils.helper import save_dataframe
from src.config.config import raw_data_path


def collect_merchants(place:str, tags:dict, filename:str):

    Logger.info(f"starting data collection for {filename}")

    gdf=ox.features_from_place(place, tags)

    Logger.info(f"Downloaded {len(gdf)} records")

    gdf = gdf.reset_index(drop=True)

    output_path = os.path.join(
        raw_data_path,
        filename
    )

    save_dataframe(
        gdf,
        output_path
    )

    Logger.info(f"Raw dataset saved at {output_path}")

    print("\n========== RAW DATA ==========")
    print(gdf.head())

    print("\nShape:")
    print(gdf.shape)

    print("\nColumns:")
    print(gdf.columns.tolist())

    print("\nRaw data collection completed successfully.")

def collect_pharmacies():

    place="Chennai, Tamil Nadu, India"

    tags={
        "amenity":"pharmacy"
    }

    filename="chennai_pharmacies.csv"

    collect_merchants(
        place=place,
        tags=tags,
        filename=filename
    )