from src.modeling.prediction import MerchantLoanPrediction


predictor = MerchantLoanPrediction()


input_data = {

    "amenity": "pharmacy",

    "healthcare": "pharmacy",

    "name": "Test Pharmacy",

    "longitude": 80.243327,

    "latitude": 13.064540,

    "nearby_hospital_count": 3,

    "nearby_bank_count": 5,

    "nearby_atm_count": 4,

    "nearby_clinic_count": 2,

    "nearby_supermarket_count": 2,

    "nearby_bus_stop_count": 4

}


result = predictor.predict(
    input_data
)


print(
    "\n========== PREDICTION =========="
)

print(
    f"Loan Eligibility: {result}"
)