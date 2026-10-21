# Building a Local FastAPI Application

A practical local API project using FastAPI, Uvicorn, Pydantic validation, and Swagger documentation.

## Objective

Build a local FastAPI application with:

- GET routes
- POST routes
- path and query parameters
- JSON request/response bodies
- Pydantic validation
- HTTP status codes
- Swagger docs at `/docs`

## Setup

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run

```powershell
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

## Routes

### GET /

```json
{
  "message": "FastAPI application is running"
}
```

### GET /health

```json
{
  "status": "healthy"
}
```

### GET /patients/{patient_id}

Example:

```text
http://127.0.0.1:8000/patients/5
```

### GET /patients?limit=5

Demonstrates a query parameter.

### POST /patients

Request:

```json
{
  "name": "Ali Khan",
  "age": 35,
  "condition": "Hypertension"
}
```

Expected status:

```text
201 Created
```

## Validation

The `Patient` Pydantic model validates:

- name: 2 to 100 characters
- age: 0 to 120
- condition: 2 to 100 characters

Invalid example:

```json
{
  "name": "A",
  "age": 500,
  "condition": ""
}
```

FastAPI automatically returns a validation error.

## Swagger Docs

Open:

```text
http://127.0.0.1:8000/docs
```

## ReDoc

```text
http://127.0.0.1:8000/redoc
```

## OpenAPI Schema

```text
http://127.0.0.1:8000/openapi.json
```

## Use in AI

FastAPI can expose AI/ML capabilities through HTTP endpoints:

```text
Client
  ↓
FastAPI
  ↓
Validated Input
  ↓
AI / ML Model
  ↓
JSON Response
```

Typical uses include model serving, LLM backends, RAG services, AI assistants, and prediction APIs.

## Safety Note

All patient examples are synthetic and only demonstrate API validation. This is not a clinical system.
