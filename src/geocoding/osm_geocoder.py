import requests

from src.utils.logger import Logger
from src.utils.exceptions import GeocodingError


def get_coordinates(
    location: str
):

    try:

        Logger.info(
            f"Searching OpenStreetMap for location: {location}"
        )

        url = "https://nominatim.openstreetmap.org/search"

        params = {
            "q": location,
            "format": "json",
            "limit": 1
        }

        headers = {
            "User-Agent": "MerchantLoanEligibilitySystem/1.0"
        }

        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        results = response.json()

        if not results:

            raise GeocodingError(
                f"Location not found: {location}"
            )

        latitude = float(
            results[0]["lat"]
        )

        longitude = float(
            results[0]["lon"]
        )

        Logger.info(
            "Location coordinates found successfully"
        )

        return (
            latitude,
            longitude
        )

    except GeocodingError:

        raise

    except Exception as e:

        Logger.error(
            f"Failed to find coordinates: {e}"
        )

        raise GeocodingError(
            "Failed to retrieve location coordinates."
        ) from e