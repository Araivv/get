import RPi.GPIO as GPIO
import time

LED = 26
state = 0
period = 1.0

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
while True:
    GPIO.output(LED, state)
    state = not state
    time.sleep(period)