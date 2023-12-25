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
   
    pregnancies = self.txtPregnancies.text
    glucose = self.txtGlucose.text
    blood_pressure = self.txtBloodPressure.text
    skin_thickness = self.txtSkinThickness.text
    insulin = self.txtInsulin.text
    bmi = self.txtBMI.text
    diabetes_pedigree_function = self.txtDiabetesPedigreeFunction.text
    age = self.txtAge.text
    alert(bmi)

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
     

     ###response = anvil.http.request('make_post_request', url, user_data)
    # result = response.json()
     #alert("Prediction: {result['prediction']}")###

     response = anvil.http.request(url="http://localhost:8000/predict/",
                    method="POST",
                    data=user_data,
                    )
     print(f"Response MIME type: {response.content_type}")

     
    except anvil.http.HttpError as e:
     print(f"Error {e.status}")
    pass

    
 

 



