import RPi.GPIO as GPIO
import time

servoPIN = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(0) # Initialization
try:
    p.ChangeDutyCycle(8)
    time.sleep(.25)
    p.ChangeDutyCycle(6)
    time.sleep(.35)
    p.stop()
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
