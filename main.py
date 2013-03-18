#-*- coding = UTF8 -*-
'''
    file : main.py
    date : 2013-3-12
    author : qlzhangtju@gmail.com
    note : 
'''
from tkinter import *
from data.dataBuf import *
from display.drawSignal import*

class Application(Tk):
    PADWIDTH = 5
    def __init__(self):
        Tk.__init__(self)
        self.wm_title("Python OSC")
        self.createWidgets()


    def createWidgets(self):
        #start button to start ECG capture
        self.startBtn = Button(self,text = "START",command = self.startFn,bd = self.PADWIDTH)
        self.startBtn.grid(row = 0,column = 2,padx = self.PADWIDTH)

        #stop button to stop ECG capture
        self.stopBtn = Button(self,text = "STOP",command = self.stopFn,bd = self.PADWIDTH)
        self.stopBtn.grid(row = 1,column = 2,padx = self.PADWIDTH)

        #disFrame to display the ECG signal
        self.disFrame = Frame(self,bd = self.PADWIDTH)
        self.disFrame.grid(row = 0,rowspan = 2)
        self.drawsignal = DrawSignal(self.disFrame)

        #stateIcon to show the state of the application
        
    
    def startFn(self):
        self.drawsignal.update(20)

    def stopFn(self):
        pass


app = Application()
app.mainloop()
