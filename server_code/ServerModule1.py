import anvil.users
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#

# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42

@anvil.server.callable
def register_user_with_google(email, display_name):
    # Implement logic to register the user using the provided email and display name
    # You can store the user information in your database or perform any additional tasks required for registration
    app_tables.users.add_row(email=email, display_name=display_name)