from Tkinter import *
import RPi.GPIO as GPIO
from time import sleep
from gpiozero import MotionSensor

CLEAR = False
LOCKED = True

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
        parent.attributes("-fullscreen", True)
        self.motion()
        self.setUpGui()

    def motion(self):
        pir.wait_for_motion()
        print ("You Moved")
        pir.wait_for_no_motion()
    
    def open(self):
        p.ChangeDutyCycle(8)
        sleep(.18)
        p.ChangeDutyCycle(0)
        LOCKED = False
        
    def close(self):
        p.ChangeDutyCycle(6)
        sleep(.16)
        p.ChangeDutyCycle(0)
        LOCKED = True

    def setUpGui(self):
        self.display = Label(self, text = "", anchor = E, bg = "white", height = 1,\
                             font = ("TexGyreAdventor", 45))
        self.display.grid(row = 0, column = 0, columnspan = 4, sticky = E + W + N + S)

        for row in range(4):
            Grid.rowconfigure(self, row, weight = 1)
        
        for col in range(3):
            Grid.columnconfigure(self, col, weight = 1)
            
        #First row of buttons
        # 1
        img = PhotoImage(file = "images/1.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda: self.process("1"))
        button.image = img
        button.grid(row = 1, column = 0, sticky = N + S + E + W)
        
        # 2
        img = PhotoImage(file = "images/2.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda: self.process("2"))
        button.image = img
        button.grid(row = 1, column = 1, sticky = N + S + E + W)
        
        # 3
        img = PhotoImage(file = "images/3.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda: self.process("3"))
        button.image = img
        button.grid(row = 1, column = 2, sticky = N + S + E + W)

        #Second row of buttons
        # 4
        img = PhotoImage(file = "images/4.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda: self.process("4"))
        button.image = img
        button.grid(row = 2, column = 0, sticky = N + S + E + W)
        
        # 5
        img = PhotoImage(file = "images/5.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda: self.process("5"))
        button.image = img
        button.grid(row = 2, column = 1, sticky = N + S + E + W)
        
        # 6
        img = PhotoImage(file = "images/6.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda: self.process("6"))
        button.image = img
        button.grid(row = 2, column = 2, sticky = N + S + E + W) 

        #Third row of buttons
        # 7
        img = PhotoImage(file = "images/7.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda: self.process("7"))
        button.image = img
        button.grid(row = 3, column = 0, sticky = N + S + E + W)
        
        # 8
        img = PhotoImage(file = "images/8.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda: self.process("8"))
        button.image = img
        button.grid(row = 3, column = 1, sticky = N + S + E + W)
        
        # 9
        img = PhotoImage(file = "images/9.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda: self.process("9"))
        button.image = img
        button.grid(row = 3, column = 2, sticky = N + S + E + W)

        #Fourth row of buttons
        # <-
        img = PhotoImage(file = "images/bak.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda: self.process("<-"))
        button.image = img
        button.grid(row = 4, column = 0, sticky = N + S + E + W)

        # 0
        img = PhotoImage(file = "images/0.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda: self.process("0"))
        button.image = img
        button.grid(row = 4, column = 1, sticky = N + S + E + W)
        
        # AC
        img = PhotoImage(file = "images/lock.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda: self.process("Locked"))
        button.image = img
        button.grid(row = 4, column = 2, sticky = N + S + E + W)

        #packs the GUI
        self.pack(fill = BOTH, expand = 1)

    def process(self, button):
        global CLEAR
        global LOCKED
        #<- deletes the newest number input        
        if (button == "<-"):
            disp = self.display ["text"]
            dispBack = disp[:-1]
            self.display ["text"] = dispBack

        elif (button == "Locked"):
            if (LOCKED == True):
                self.display["text"] = "Already Locked"
                CLEAR = True

            if (LOCKED == False):
                if (CLEAR == True):
                    self.display["text"] = ""
                    self.close()
                    self.display["text"] += button
                    LOCKED = True
            
        else:
            #limits the user from inputting more than 4
            #and also clears display after encountering an ERROR
            #or hitting "="
            if (len(self.display["text"]) < 4):
                if (CLEAR == True):
                    self.display["text"] = ""
                    self.display["text"] += button
                    CLEAR = False
                else:
                    self.display["text"] += button
            else:
                if (CLEAR == True):
                    self.display["text"] = ""
                    self.display["text"] += button
                    CLEAR = False
                else:
                    self.display["text"] = ""

        if (self.display["text"] == "1894" and LOCKED == True):
            LOCKED = False
            self.display["text"] = "Unlocked"
            self.open()
            CLEAR = True
                
            
            
    
            

window = Tk()
window.title("Lockbox GUI")

c = GUI(window)

window.mainloop()

