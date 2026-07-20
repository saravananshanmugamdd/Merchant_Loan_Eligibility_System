from haversine import haversine, Unit

def calculate_distance(
        latitude_1=float,
        longitude_1=float,
        latitude_2=float,
        longitude_2=float
) -> float:
    
    point_1=(
        latitude_1,
        longitude_1
    )

    point_2=(
        latitude_2,
        longitude_2
    )

    distance=haversine(
        point_1,
        point_2,
        unit=Unit.METERS
    )

    return distance