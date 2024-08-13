from fraud_detection.models import FraudData
from fraud_detection.utils import *
import pickle


def getFraudDetectionModel(model):
    try:
        if fraudModelsSrc[model] == None:
            raise "Fraud detection model requested not found."
        with open(fraudModelsSrc[model], "rb") as f:
            model = pickle.load(f)
        return model
    except Exception as e:
        print("Error loading model:", e)
        raise e


class FraudDetectionClassifier:
    def __init__(self):
        pass

    def classify_fraud_detection(self, fraud_data: FraudData):
        X = [
            fraud_data.name_email_similarity,
            fraud_data.current_address_months_count,
            fraud_data.credit_risk_score,
            fraud_data.housing_status,
            fraud_data.velocity_6h,
            fraud_data.bank_branch_count_8w,
            fraud_data.employment_status,
            fraud_data.prev_address_months_count,
        ]
        print("Features:", X)
        model = getFraudDetectionModel("random-forest")
        print("Model", model)
        return
