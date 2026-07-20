from src.feature_engineering.distance_calculator import calculate_distance

def count_nearby_places(
        source_df,
        target_df,
        radius=500
):
    nearby_counts=[]

    for _, source_row in source_df.iterrows():
        count=0
        for _, target_row in target_df.iterrows():
            
            distance=calculate_distance(
                source_row["latitude"],
                source_row["longitude"],
                target_row["latitude"],
                target_row["longitude"]
            )

            if (
                distance <= radius
                and source_row.name != target_row.name
            ):
                count+=1
        nearby_counts.append(count)
    return nearby_counts

