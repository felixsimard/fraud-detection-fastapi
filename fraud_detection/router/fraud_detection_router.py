from typing import List
from fastapi import APIRouter
from starlette.responses import JSONResponse
from fastapi import UploadFile
from fraud_detection.classifier import FraudDetectionClassifier
from fraud_detection.models import FraudData

router = APIRouter()


@router.post("/predict")
def predict(inputs: List[List]):
    try:
        print("Inputs:", inputs)
        classifier = FraudDetectionClassifier()
        # prediction = classifier.predict(inputs)
        return JSONResponse({"prediction": "0.0"})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
