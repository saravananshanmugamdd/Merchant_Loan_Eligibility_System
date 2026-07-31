from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.modeling.prediction import MerchantLoanPrediction
from src.geocoding.osm_geocoder import get_coordinates
from src.utils.logger import Logger
from src.utils.exceptions import GeocodingError


app = FastAPI(
    title="Merchant Loan Eligibility API",
    description="API for predicting merchant loan eligibility",
    version="1.0.0"
)


class LoanPredictionRequest(BaseModel):

    pharmacy_name: str
    location: str


class LoanPredictionResponse(BaseModel):

    pharmacy_name: str
    location: str
    latitude: float
    longitude: float
    loan_eligibility: str
    nearby_features: dict


try:

    predictor = MerchantLoanPrediction()

    Logger.info(
        "Prediction Pipeline Initialized Successfully"
    )

except Exception as e:

    Logger.error(
        f"Failed to initialize prediction pipeline: {e}"
    )

    predictor = None


@app.get("/")
def home():

    return {
        "message": "Merchant Loan Eligibility API is running"
    }


@app.get("/health")
def health_check():

    if predictor is None:

        return {
            "status": "unhealthy"
        }

    return {
        "status": "healthy"
    }


@app.post(
    "/predict",
    response_model=LoanPredictionResponse
)
def predict_loan(
    request: LoanPredictionRequest
):

    if predictor is None:

        raise HTTPException(
            status_code=500,
            detail="Prediction pipeline is not available."
        )

    try:

        search_location = (
            f"{request.pharmacy_name}, "
            f"{request.location}"
        )

        latitude, longitude = get_coordinates(
            search_location
        )

        prediction_result = predictor.predict(
            latitude=latitude,
            longitude=longitude
        )

        return LoanPredictionResponse(
            pharmacy_name=request.pharmacy_name,
            location=request.location,
            latitude=latitude,
            longitude=longitude,
            loan_eligibility=prediction_result["prediction"],
            nearby_features=prediction_result["features"]
            )

    except GeocodingError as e:

        Logger.error(
            f"Geocoding failed: {e}"
        )

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


    except Exception as e:

        Logger.error(
            f"Prediction API Failed: {e}"
        )

        raise HTTPException(
            status_code=500,
            detail="Failed to generate loan eligibility prediction."
        )