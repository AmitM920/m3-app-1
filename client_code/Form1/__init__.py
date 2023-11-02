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
