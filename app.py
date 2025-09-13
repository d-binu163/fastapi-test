# Import all libraries needed
from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib

# Create the FastAPI instance
app = FastAPI()

# Load the trained model
model = joblib.load('diabetes_model.pkl')

# Define the input schema with constraints
class PatientData(BaseModel):
    age: int = Field(..., ge=0, le=120, description="Age in years (0–120)")
    sex: int = Field(..., ge=0, le=1, description="Sex (0 = female, 1 = male)")
    bmi: float = Field(..., gt=0, lt=100, description="Body Mass Index")
    bp: float = Field(..., gt=0, lt=200, description="Blood Pressure")
    s1: float 
    s2: float 
    s3: float 
    s4: float
    s5: float
    s6: float

# Define a POST endpoint using /predict
@app.post("/predict")

def predict(data: PatientData):
    # Convert input data to the right format - This is crucial because scikit-learn models expect a 2D array of features.
    features = [
        data.age, data.sex, data.bmi, data.bp,
        data.s1, data.s2, data.s3, data.s4,
        data.s5, data.s6
    ]
    
    # Call your ML model’s predict method with features wrapped inside [ ] → makes it a 2D array ([ [age, sex, ...] ]).
    prediction = model.predict([features])

    # Takes the first prediction, converts it to an int (since NumPy types don’t serialize easily) and return as JSON
    return {"prediction": int(prediction[0])}
