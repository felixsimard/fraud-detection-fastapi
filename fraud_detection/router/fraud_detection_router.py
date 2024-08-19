from typing import List
from fastapi import APIRouter
from starlette.responses import JSONResponse
import random
import numpy as np
from fraud_detection.classifier import FraudDetectionClassifier
from fraud_detection.models import FraudData

router = APIRouter()


@router.post("/predict")
def predict(inputs: List[List]):
    try:
        header = inputs[0]
        rows = inputs[1:]

        # Init classifier
        classifier = FraudDetectionClassifier()

        # Output
        fraudulent_entries = []

        # Classify each input
        for row in rows:
            fraud_data = FraudData(
                name_email_similarity=row[0],
                current_address_months_count=row[1],
                credit_risk_score=row[2],
                housing_status=row[3],
                velocity_6h=row[4],
                bank_branch_count_8w=row[5],
                employment_status=row[6],
                prev_address_months_count=row[7],
            )
            fraud_detected = classifier.classify_fraud_detection(
                header=header, fraud_data_row=fraud_data
            )
            if fraud_detected:
                fraudulent_entries.append(row)

        if len(fraudulent_entries) == 0:
            # For demonstration purposes, if no entries detected as fraudulent by the model, detect some randomly
            sample = random.sample(population=rows, k=random.randint(0, 25))
            fraudulent_entries = sample

        return JSONResponse(fraudulent_entries)
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
