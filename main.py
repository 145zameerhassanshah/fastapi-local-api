from fastapi import FastAPI, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="Local FastAPI Practice",
    description="A local API demonstrating GET and POST routes, Pydantic validation, and Swagger docs.",
    version="1.0.0",
)


class Patient(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    age: int = Field(ge=0, le=120)
    condition: str = Field(min_length=2, max_length=100)


@app.get("/")
def home():
    return {"message": "FastAPI application is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/patients/{patient_id}")
def get_patient(patient_id: int):
    return {
        "patient_id": patient_id,
        "message": "Patient route accessed successfully",
    }


@app.get("/patients")
def list_patients(limit: int = 10):
    return {
        "limit": limit,
        "message": "Query parameter received successfully",
    }


@app.post("/patients", status_code=status.HTTP_201_CREATED)
def create_patient(patient: Patient):
    return {
        "message": "Patient data validated successfully",
        "patient": patient,
    }
