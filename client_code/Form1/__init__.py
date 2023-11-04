from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
  
    
    

    # Any code you write here will run before the form opens.

  def image_1_mouse_enter(self, x, y, **event_args):
    """This method is called when the mouse cursor enters this component"""
    pass

  def image_1_show(self, **event_args):
    """This method is called when the Image is shown on the screen"""
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pregnancies = self.txtPregnancies.text
    glucose = self.txtGlucose.text
    blood_pressure = self.txtBloodPressure.text
    skin_thickness = self.txtSkinThickness.text
    insulin = self.txtInsulin.text
    bmi = self.txtBMI.text
    diabetes_pedigree_function = self.txtDiabetesPedigreeFunction.text
    age = self.txtAge.text

    # Create a dictionary with user input data
    user_data = {
        "Pregnancies": pregnancies,
        "Glucose": glucose,
        "BloodPressure": blood_pressure,
        "SkinThickness": skin_thickness,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": diabetes_pedigree_function,
        "Age": age
        # Add other input fields here
    }

    # Define the URL of your FastAPI endpoint
    url = "http://your-fastapi-url/predict/"

    # Make an HTTP POST request to your FastAPI endpoint
    response = anvil.server.http.request(url, json=user_data)

    # Handle the response from your FastAPI backend
    if response.status_code == 200:
        # If the response status code is 200 (OK), you can access the result
        result = response.json()
        # Do something with the result (e.g., display it to the user)
    else:
        # Handle the case where the request was not successful
        # (you can display an error message to the user)
   

