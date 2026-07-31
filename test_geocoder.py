from src.collectors.osm_geocoder import get_coordinates


location = "Apollo Pharmacy, Anna Nagar, Chennai"


latitude, longitude = get_coordinates(
    location
)


print(
    "\n========== LOCATION =========="
)

print(
    f"Location: {location}"
)

print(
    f"Latitude: {latitude}"
)

print(
    f"Longitude: {longitude}"
)