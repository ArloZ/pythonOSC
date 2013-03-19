#-*- coding = UTF8 -*-
'''
    file : main.py
    date : 2013-3-12
    author : qlzhangtju@gmail.com
    note : 
'''

from data.dataConvert import *
from display.drawSignal import *
from display.disState import *
from capture.commUart import*


class Application(Tk):
    PADWIDTH = 5
    def __init__(self):
        Tk.__init__(self)
        self.wm_title("Python OSC")
        self.createWidgets()
        self.comm = CommUart(0)
        self.comm.setRecCbk(self.commRecCbk,3)
        self.comm.start()
        self.conv = DataConvert(23,2.42,0)

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
        self.comm.sendHex(1)

    def stopFn(self):
        self.disstate.setState("stop")
        self.comm.sendHex(0)
        
    
    def commRecCbk(self):
        data = self.comm.receive()
        val = 0
        for v in data:
            val = (val << 8) + v
        print("before convert:",val)
        x = self.conv.convert(val)
        print("after convert:",x)


app = Application()
app.mainloop()
