'''from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.preprocessing import StandardScaler
import numpy as np
import pickle

app = FastAPI()



# Load the trained model (replace 'classifier.pkl' with your model file name)
with open('classifier.pkl', 'rb') as model_file:
    classifier = pickle.load(model_file)

# Create a Pydantic model to define the request structure
class PredictionInput(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

scaler = StandardScaler()
scaler.fit(X)  # Assuming X is your data for training the scaler


# Define the API route
@app.post("/predict/")
async def predict(input_data: PredictionInput):
    data = [input_data.Pregnancies, input_data.Glucose, input_data.BloodPressure,
            input_data.SkinThickness, input_data.Insulin, input_data.BMI,
            input_data.DiabetesPedigreeFunction, input_data.Age]

    # Standardize the input data
    standarized_data = scaler.transform([data])
    
    # Predict using the loaded model
    prediction = classifier.predict(standarized_data)
    
    result = "The person is Diabetic" if prediction == 1 else "The person is Non-Diabetic"
    return {"prediction": int(prediction[0]), "result": result}
'''
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.preprocessing import StandardScaler
import pickle
import numpy as np
import pandas as ap
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this with the appropriate origins for your frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data Loading Function
import pandas as pd

def load_diabetes_data():
    # Load the diabetes dataset
    diabetes_dataset = pd.read_csv("diabetes.csv")

    # Preprocess the data if needed
    # For example, drop any unnecessary columns or perform feature engineering.

    # Return the features (X) and target (Y)
    X = diabetes_dataset.drop(columns='Outcome', axis=1)
    Y = diabetes_dataset['Outcome']

    return X, Y

# Load the trained model
with open('classifier.pkl', 'rb') as model_file:
    classifier = pickle.load(model_file)

# Create a StandardScaler instance
scaler = StandardScaler()
X, Y = load_diabetes_data()
scaler.fit(X)

# Define the Pydantic model for request data
class PredictionInput(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int
@app.get("/")
async def homepage():
    return {"message": "Welcome to the Diabetes Prediction API"}    

# Define the API route for prediction
@app.post("/predict")
async def predict(input_data: PredictionInput):
    data = [input_data.Pregnancies, input_data.Glucose, input_data.BloodPressure,
            input_data.SkinThickness, input_data.Insulin, input_data.BMI,
            input_data.DiabetesPedigreeFunction, input_data.Age]
    

    # Standarize the input data
    standarized_data = scaler.transform([data])

    # Predict using the loaded model
    prediction = classifier.predict(standarized_data)

    return {"prediction": int(prediction[0])}
