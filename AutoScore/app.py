from flask import Flask, render_template
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

triggerPin = 7
echoPin = 11

# Score variable
score = 0

# Setup GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(triggerPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

# Function to update score
def update_score(distance, score):
    # CHANGE depending on basketball hoop size
    if distance < 20:
        score += 1
    return score

# Function to measure distance and update score
def measure_distance():
    # Reset variables
    pulse_start = 0
    pulse_end = 0

    # Send ultrasonic signal
    GPIO.output(triggerPin, GPIO.LOW)
    time.sleep(0.2)

    GPIO.output(triggerPin, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(triggerPin, GPIO.LOW)

    # Measure distance
    while GPIO.input(echoPin) == 0:
        pulse_start = time.time()

    while GPIO.input(echoPin) == 1:
        pulse_end = time.time()

    duration = pulse_end - pulse_start
    distance_cm = duration * 34300 / 2

    # Update score
    global score
    score = update_score(distance_cm, score)

    return distance_cm, score

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/score')
def get_score():
    distance, score = measure_distance()
    return {'distance': distance, 'score': score}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
