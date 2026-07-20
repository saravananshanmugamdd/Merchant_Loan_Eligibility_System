import os
import osmnx as ox

from src.utils.logger import Logger
from src.utils.helper import save_dataframe
from src.config.config import raw_data_path


def collect_osm_data(
        place:str, 
        tag_key:str,
        tag_value:str, 
        filename:str
    ):

    Logger.info(f"starting data collection for {filename}")

    tags = {
        tag_key: tag_value
        }

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

