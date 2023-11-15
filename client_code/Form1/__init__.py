from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.http

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
    alert("this messages shows when button is clicked")
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
    try:
    # Make an HTTP POST request using Anvil's HTTP services
     response = anvil.http.request('make_post_request', url, user_data)

    # Handle the response from your FastAPI backend
     if response.status_code == 200:
        # If the response status code is 200 (OK), you can access the result
        result = response.json()
        # Display result to the user
        self.label_result.text = f"Prediction: {result['prediction']}"
        # Clear input fields
        self.clear_input_fields()
     else:
        # Handle the case where the request was not successful
        # Display an error message to the user
        alert(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
     alert(f"An error occurred: {str(e)}")

def clear_input_fields(self):
    """Clear input fields after submitting the form"""
    self.txtPregnancies.text = ""
    self.txtGlucose.text = ""
    self.txtBloodPressure.text = ""
    self.txtSkinThickness.text = ""
    self.txtInsulin.text = ""
    self.txtBMI.text = ""
    self.txtDiabetesPedigreeFunction.text = ""
    self.txtAge.text = ""
    # Clear other input fields if needed