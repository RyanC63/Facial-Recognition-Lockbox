from Tkinter import *
import RPi.GPIO as GPIO
from time import sleep

servoPIN = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(0) # Initialization

class GUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.setUpGui()

    def open(self):
        p.ChangeDutyCycle(8)
        sleep(.115)
        p.ChangeDutyCycle(0)
    
    def close(self):
        p.ChangeDutyCycle(6)
        sleep(.1)
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
