import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LED = 26
GPIO.setup(LED, GPIO.OUT)


state = 0
pwm = GPIO.PWM(LED,200)
duty = 0.0
pwm.start(duty)

while True:
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.05)

    GPIO.output(LED, state)

    duty+=1.0
    if duty>100:
        duty = 0