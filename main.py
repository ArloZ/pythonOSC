#-*- coding = UTF8 -*-
'''
    file : main.py
    date : 2013-3-12
    author : qlzhangtju@gmail.com
    note : 
'''

from data.dataBuf import *
from display.drawSignal import *
from display.disState import *
from capture.commUart import*


class Application(Tk):
    PADWIDTH = 5
    def __init__(self):
        Tk.__init__(self)
        self.wm_title("Python OSC")
        self.createWidgets()
        self.comm = CommUart(1)

    def createWidgets(self):
        #stateIcon to show the state of the application
        self.sIcon = Frame(self,bd = self.PADWIDTH)
        self.sIcon.grid(row = 0,column = 2,padx = self.PADWIDTH)
        self.disstate = DisState(self.sIcon)
        
        #start button to start ECG capture
        self.startBtn = Button(self,text = "START",command = self.startFn,bd = self.PADWIDTH)
        self.startBtn.grid(row = 1,column = 2,padx = self.PADWIDTH)

        #stop button to stop ECG capture
        self.stopBtn = Button(self,text = "STOP",command = self.stopFn,bd = self.PADWIDTH)
        self.stopBtn.grid(row = 2,column = 2,padx = self.PADWIDTH)

        #disFrame to display the ECG signal
        self.disFrame = Frame(self,bd = self.PADWIDTH)
        self.disFrame.grid(row = 0,rowspan = 3)
        self.drawsignal = DrawSignal(self.disFrame)


    
    def startFn(self):
        self.disstate.setState("start")
        self.drawsignal.update(20)

    def stopFn(self):
        self.disstate.setState("stop")
        pass


app = Application()
app.mainloop()
