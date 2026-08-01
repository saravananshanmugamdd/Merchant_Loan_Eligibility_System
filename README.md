# Merchant Loan Eligibility Prediction System

An end-to-end Machine Learning application that predicts merchant loan eligibility based on nearby business-supporting facilities such as hospitals, banks, ATMs, clinics, supermarkets, and bus stops.

The system uses OpenStreetMap data for geospatial information, performs data preprocessing and feature engineering, trains and evaluates multiple Machine Learning models, and provides predictions through a FastAPI backend and Streamlit frontend.

> **Note:** This project uses a proxy eligibility target for proof-of-concept purposes. The model is not trained on real historical loan approval or repayment data. Production deployment would require validated historical merchant loan data.

## Features

* OpenStreetMap-based data collection
* Coordinate processing
* Data cleaning
* Missing and null value handling
* Duplicate handling
* Datatype validation
* Nearby facility feature engineering
* Feature validation
* Train/test dataset preparation
* Multiple Machine Learning models
* Model evaluation and comparison
* Best model selection
* Final model generation
* Custom exception handling
* Logging
* OpenStreetMap geocoding
* FastAPI REST API
* Pydantic request and response validation
* Streamlit frontend
* End-to-end loan eligibility prediction

## Nearby Features

The system generates the following features based on the merchant's location:

* `nearby_hospital_count`
* `nearby_bank_count`
* `nearby_atm_count`
* `nearby_clinic_count`
* `nearby_supermarket_count`
* `nearby_bus_stop_count`

These features are generated dynamically for the submitted pharmacy location and passed to the final Machine Learning model.

## Machine Learning Models

The following classification algorithms were trained and evaluated:

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier
* K-Nearest Neighbors
* Gaussian Naive Bayes
* Support Vector Machine

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score

The best-performing model was selected based on F1 Score and saved as the final model.

## Technologies Used

### Programming Language

* Python

### Data Processing

* Pandas
* NumPy

### Geospatial Data

* GeoPandas
* OpenStreetMap
* OSMnx
* Nominatim

### Machine Learning

* Scikit-learn
* Joblib

### Backend

* FastAPI
* Pydantic
* Uvicorn

### Frontend

* Streamlit

### Version Control

* Git
* GitHub

## Installation

Clone the repository:

```bash
git clone <your-github-repository-url>
```

Navigate to the project:

```bash
cd Merchant_Loan_Eligibility_system
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Machine Learning Pipeline

The Machine Learning pipeline consists of the following stages:

1. Data Collection
2. Coordinate Processing
3. Data Cleaning
4. Null Value Handling
5. Duplicate Handling
6. Datatype Handling
7. Feature Engineering
8. Feature Validation
9. Train/Test Split
10. Model Training
11. Model Evaluation
12. Best Model Selection
13. Final Model Generation

The pipeline can be executed through the project `main.py` file using the configured stages.

Example:

```bash
python main.py --stage collect
```

```bash
python main.py --stage preprocess
```

```bash
python main.py --stage features
```

```bash
python main.py --stage validate
```

```bash
python main.py --stage split
```

```bash
python main.py --stage train
```

```bash
python main.py --stage evaluate
```

## FastAPI Backend

The FastAPI application provides the prediction API.

Start the FastAPI server:

```bash
uvicorn src.api.app:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

API documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## Health Check

The health endpoint is:

```text
GET /health
```

Example response:

```json
{
    "status": "healthy"
}
```

## Prediction API

The prediction endpoint is:

```text
POST /predict
```

Example request:

```json
{
    "pharmacy_name": "Apollo Pharmacy",
    "location": "Anna Nagar, Chennai"
}
```

The system performs the following operations:

1. Receives the pharmacy name and location.
2. Sends the location to OpenStreetMap Nominatim.
3. Retrieves latitude and longitude.
4. Generates nearby facility features.
5. Sends the generated features to the final Machine Learning model.
6. Predicts loan eligibility.
7. Returns the prediction and location information.

Example response:

```json
{
    "pharmacy_name": "Apollo Pharmacy",
    "location": "Anna Nagar, Chennai",
    "latitude": 13.08,
    "longitude": 80.21,
    "loan_eligibility": "Eligible",
    "nearby_features": {
        "nearby_hospital_count": 3,
        "nearby_bank_count": 5,
        "nearby_atm_count": 2,
        "nearby_clinic_count": 2,
        "nearby_supermarket_count": 0,
        "nearby_bus_stop_count": 4
    }
}
```

The exact coordinates and prediction depend on the submitted location and trained model.

## Streamlit Frontend

The Streamlit application provides the user interface.

Start Streamlit:

```bash
streamlit run src/frontend/app1.py
```

The user can enter:

```text
Pharmacy Name: Apollo Pharmacy
Location: Anna Nagar, Chennai
```

The application communicates with the FastAPI backend and displays:

* Pharmacy name
* Location
* Latitude
* Longitude
* Nearby hospitals
* Nearby banks
* Nearby ATMs
* Nearby clinics
* Nearby supermarkets
* Nearby bus stops
* Loan eligibility result

## Running the Application

The FastAPI backend and Streamlit frontend must be running simultaneously.

Start FastAPI in the first terminal:

```bash
uvicorn src.api.app:app --reload
```

Start Streamlit in the second terminal:

```bash
streamlit run src/frontend/app1.py
```

The user can then access the Streamlit application through the browser.

## Application Workflow

The application follows this workflow:

User enters pharmacy name and location.

The Streamlit frontend sends the request to FastAPI.

FastAPI sends the location to OpenStreetMap Nominatim.

Latitude and longitude are retrieved.

Nearby facility features are generated.

The generated features are passed to the final Machine Learning model.

The model predicts:

* Eligible
* Not Eligible

The prediction and nearby facility information are returned to the Streamlit frontend.

## Error Handling

The project uses custom exceptions for different stages of the application, including:

* `DataCollectionError`
* `CoordinateExtractionError`
* `DataCleaningError`
* `DataValidationError`
* `FeatureEngineeringError`
* `ModelTrainingError`
* `PredictionError`
* `GeocodingError`

The application also uses logging to track pipeline execution and errors.

## Target Variable

The current project uses:

```text
loan_eligibility_proxy
```

as the target variable.

This is a proxy target created for demonstrating the complete Machine Learning workflow.

Therefore, this project should be considered a Proof of Concept rather than a production-ready financial decision system.

For real-world deployment, the model should be trained using validated historical merchant loan data containing relevant financial and business information.

Potential real-world features could include:

* Merchant revenue
* Monthly transaction volume
* Average transaction value
* Business age
* Credit history
* Existing loan obligations
* Repayment history
* Bank transaction patterns
* Actual loan approval outcomes
* Actual loan default outcomes

## Future Improvements

* Replace the proxy target with real historical loan data
* Add merchant transaction features
* Add credit-related features
* Add business revenue and age features
* Add cross-validation
* Add model hyperparameter tuning
* Add unit and integration tests
* Add Docker support
* Add CI/CD pipeline
* Deploy the FastAPI backend
* Deploy the Streamlit frontend
* Add database integration
* Add authentication and authorization
* Add model monitoring
* Add data drift monitoring

## Disclaimer

This project is developed for educational and proof-of-concept purposes.

The current model uses a proxy target and should not be used to make real financial or lending decisions.

A production lending system requires validated financial data, regulatory compliance, fairness and bias testing, security controls, model governance, and continuous monitoring.
