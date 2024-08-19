FROM python:3.11


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# EXPOSE 5000

# CMD ["uvicorn", "--host", "0.0.0.0", "--port", "5000", "iris.app:app"]

# if running behind a TLS load balancer, add --proxy-headers
CMD ["fastapi", "run", "fraud_detection/app.py", "--port", "5001"] 