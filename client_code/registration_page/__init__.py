from ._anvil_designer import registration_pageTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class registration_page(registration_pageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  

  def sign_in_with_google_click_click(self, **event_args):
    """This method is called when the button is clicked"""
    try:
        # Initiate the Google Sign-In process
        user = anvil.google.auth.sign_in_with_google()
        
        # Optionally, you can access user information such as email and display name
        email = user['email']
        display_name = user['display_name']
        
        # You can use the user information for further processing or registration
        # For example, call a server function to register the user using their Google account
        
        # Display a success message to the user
        alert(f"Google Sign-In successful! Welcome, {display_name}.")
        
    except Exception as e:
        # Handle any errors that occur during Google Sign-In
        alert(f"Google Sign-In failed: {str(e)}")
    pass
  def register_user(self, email, display_name):
        # Call the server function to register the user
        anvil.server.call('register_user', email, display_name) 
