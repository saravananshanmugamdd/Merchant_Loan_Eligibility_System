import os
import geopandas as gpd

from src.utils.logger import Logger
from src.utils.helper import load_dataframe, save_dataframe
from src.config.config import raw_data_path, processed_data_path


def coordinate_pipeline():

    Logger.info("Coordinate Pipeline Started")

    input_path = os.path.join(
        raw_data_path,
        "chennai_pharmacies.csv"
    )

    df = load_dataframe(input_path)

    print("\nRaw Shape:")
    print(df.shape)

    # Convert geometry column into GeoDataFrame
    gdf = gpd.GeoDataFrame(
        df,
        geometry=gpd.GeoSeries.from_wkt(df["geometry"]),
        crs="EPSG:4326"
    )

    # Convert to projected CRS for accurate centroid calculation
    projected_gdf = gdf.to_crs(epsg=32644)

    projected_gdf["centroid"] = projected_gdf.geometry.centroid

    centroid_gdf = projected_gdf.set_geometry(
        "centroid"
    ).to_crs(epsg=4326)

    # Extract longitude and latitude
    gdf["longitude"] = centroid_gdf.geometry.x
    gdf["latitude"] = centroid_gdf.geometry.y

    print("\nCoordinates Added Successfully")
    print(gdf[["longitude", "latitude"]].head())

    # Save processed dataset
    output_path = os.path.join(
        processed_data_path,
        "chennai_pharmacies_coordinates.csv"
    )

    save_dataframe(
        gdf,
        output_path
    )

    Logger.info("Coordinate Pipeline Completed")

    print("\nProcessed Shape:")
    print(gdf.shape)

    print("\nCoordinate dataset saved successfully.")