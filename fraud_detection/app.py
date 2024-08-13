from fastapi import FastAPI
from fraud_detection.router import fraud_detection_router

app = FastAPI()
app.include_router(fraud_detection_router.router, prefix="/fraud-detection")


@app.get("/healthcheck", status_code=200)
async def healthcheck():
    return "Fraud Detection is all ready to go!"
