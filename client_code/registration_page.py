from anvil import HtmlPanel, Button

# Define a function to handle button click event
def button_click_handler(self, **event_args):
    alert("Button clicked!")

# Create an instance of HtmlPanel
html_panel_1 = HtmlPanel()

# Add custom HTML content to the HtmlPanel
html_panel_1.content = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Login Page</title>
<style>
  body {
    background-color: #f5f5dc; /* light beige */
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
  .login-container {
    text-align: center;
  }
  h1 {
    font-size: 2.5rem;
    color: #333;
  }
  .button-container {
    margin-top: 30px;
  }
  .button {
    padding: 10px 20px;
    font-size: 1.2rem;
    border-radius: 5px;
    cursor: pointer;
    margin-right: 10px;
    border: none;
  }
  .login-button {
    background-color: #4285f4; /* Google blue */
    color: #fff;
  }
  .manual-button {
    background-color: #4caf50; /* Green */
    color: #fff;
  }
  h2{
    font-size: 2.0 rem;
    color:#333;
  }
</style>
</head>
<body>
  <div class="login-container">
    <h1>Glucomotion:</h1>
    <div class ="login-container-second-line"><h2>Your Personal Diabetes Wellness Companion App</h2></div>
    <div class="button-container">
      <button class="button login-button">Login using Google</button>
      <button class="button manual-button">Manual Login</button>
    </div>
  </div>
</body>
</html>
"""

# Create an instance of Button
button_1 = Button(text="Anvil Button")

# Set event handler for the Button
button_1.set_event_handler('click', button_click_handler)

# Add components to the app
app_content = [html_panel_1, button_1]