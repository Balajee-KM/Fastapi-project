from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

class SensorData(BaseModel):
    temperature: float
    humidity: float
    timestamp: str

@app.post("/upload")
def upload_data(data: SensorData):
    print("Received:", data)
    return {"status": "success", "data": data}