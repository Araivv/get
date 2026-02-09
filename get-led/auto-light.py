import RPi.GPIO as GPIO

LED = 26
state = 0
PHOTORESISTER = 6

GPIO.setmode(GPIO.BCM)

GPIO.setup(PHOTORESISTER, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

while True:
    if GPIO.input(PHOTORESISTER):
        state = 0
        GPIO.output(LED, state)
    else:
        state = 1
        GPIO.output(LED, state)