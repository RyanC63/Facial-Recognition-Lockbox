from Tkinter import *
import RPi.GPIO as GPIO
from time import sleep
from gpiozero import MotionSensor

#sets ups pins
servoPIN = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(0) # Initialization

pir = MotionSensor(6)

class GUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        sense = self.motion()
        self.setUpGui()

    def motion(self):
        pir.wait_for_motion()
        print ("You Moved")
        sense = True
        return sense
        pir.wait_for_no_motion()
    
    def open(self):
        p.ChangeDutyCycle(8)
        sleep(.18)
        p.ChangeDutyCycle(0)
        
    def close(self):
        p.ChangeDutyCycle(6)
        sleep(.16)
        p.ChangeDutyCycle(0)

    def setUpGui(self):
        self.pack(fill = BOTH, expand = 1)

        GUI.unlock_button = Button(self, text = "Unlock", fg = "black",\
                                   command = lambda: self.open())
        GUI.unlock_button.pack(side = BOTTOM, fill = X)

        GUI.lock_button = Button(self, text = "Lock", fg = "black",\
                                 command = lambda: self.close())
        GUI.lock_button.pack(side = TOP, fill = X)



window = Tk()
window.title("Dummy Thicc")

c = GUI(window)

window.mainloop()
