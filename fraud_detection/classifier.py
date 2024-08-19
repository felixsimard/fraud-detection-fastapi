from typing import List
from fraud_detection.models import FraudData
from fraud_detection.utils import *
import numpy as np


class FraudDetectionClassifier:
    def __init__(self):
        pass

    def classify_fraud_detection(self, header: List[str], fraud_data_row: FraudData):
        X = [
            fraud_data_row.name_email_similarity,
            fraud_data_row.current_address_months_count,
            fraud_data_row.credit_risk_score,
            fraud_data_row.housing_status,
            fraud_data_row.velocity_6h,
            fraud_data_row.bank_branch_count_8w,
            fraud_data_row.employment_status,
            fraud_data_row.prev_address_months_count,
        ]

        # Define model
        model_name = "random-forest"

        # Load model pkl
        model_pkl = getFraudDetectionModel(model_name)

        # Get appropriate features for this model
        features = getModelFeatures(model_name)

        # Create a list of the feature indexes within the readerList
        # This will be used to get the feature values from the readerList for each data row
        featuresIndexes = [header.index(feature) for feature in features]

        # Get the feature values for the current row
        featureValues = [X[i] for i in featuresIndexes]

        # Predict
        prediction = model_pkl.predict(np.array([featureValues]))
        fraud_detected = True if prediction[0] == 1 else False

        return fraud_detected
