class MerchantLoanException(Exception):
    pass

class DataCollectionError(MerchantLoanException):
    pass

class CoordinateExtractionError(MerchantLoanException):
    pass

class DataCleaningError(MerchantLoanException):
    pass

class DataValidationError(MerchantLoanException):
    pass

class InvalidCoordinateError(MerchantLoanException):
    pass

class FeatureEngineeringError(MerchantLoanException):
    pass

class ModelTrainingError(MerchantLoanException):
    pass

class PredictionError(MerchantLoanException):
    pass
