from ._anvil_designer import loginTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class login(loginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    anvil.users.login_with_form()
  def button_1_show(self, **event_args):
   """This method is called when the Button is shown on the screen"""
   open_form('content_page')
  pass
    # Any code you write here will run before the form opens.


       