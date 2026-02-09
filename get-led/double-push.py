import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

LEDS = [24, 22, 23, 27, 17, 25, 12, 16]
BUTTON_PLUS = 10
BUTTON_MINUS = 9

GPIO.setup(LEDS, GPIO.OUT)
GPIO.setup(BUTTON_PLUS, GPIO.IN)
GPIO.setup(BUTTON_MINUS, GPIO.IN)
GPIO.output(LEDS, 0)

num=0
sleep_time = 0.2
pressed = False

while True:
    if pressed:
        GPIO.output(LEDS, dec2bin(0))
        pressed = False

    if GPIO.input(BUTTON_PLUS) == 1 and GPIO.input(BUTTON_MINUS) == 1 and pressed == False:
        GPIO.output(LEDS, dec2bin(255))
        pressed = True

    if GPIO.input(BUTTON_PLUS):
        num = min((num + 1),255)
        time.sleep(sleep_time)
        pressed = False
    if GPIO.input(BUTTON_MINUS):
        num = max((num - 1), 0)
        time.sleep(sleep_time)
        pressed = False
    GPIO.output(LEDS, dec2bin(num))  
        