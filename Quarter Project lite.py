from Tkinter import *
from time import sleep
from picamera import PiCamera

class GUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.setUpGui()

    def setUpGui(self):
        self.pack(fill = BOTH, expand = 1)

        GUI.take_picture_button = Button(self, text = "Take Picture",\
                                         fg = "black",\
                                         command = lambda: self.take_picture())
        GUI.take_picture_button.pack(side = BOTTOM, fill = X)
        
        GUI.quit_button = Button(self, text = "QUIT", fg = "red",\
                                 command = quit)
        GUI.quit_button.pack(side = TOP, fill = X)

    def take_picture(self):
        camera = PiCamera()
        camera.resolution = (1024, 768)
        camera.start_preview()
        sleep(3)
        camera.capture("face.jpg")
        camera.stop_preview()

###########################################################
window = Tk()
window.title("Dummy Thicc")

c = GUI(window)

window.mainloop()
