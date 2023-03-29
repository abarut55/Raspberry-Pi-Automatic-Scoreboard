# Raspberry-Pi-Automatic-Scoreboard
An automatic scoreboard is a device that will automatically display the score of a sports game.


app.py: This modified code sets up a global variable called score to keep track of the score. In the home() function, the distance() function is called to measure the distance from the HC-SR04 sensor. If the distance is less than or equal to 1000 cm, the score variable is incremented by 1.

Then, the render_template() function is called to render the "index.html" template with the current value of score passed as a variable. The updated score value is displayed in the HTML.

index.html: displays it.

KEY NOTES: Any updates for app.py file please comment what was changed!
