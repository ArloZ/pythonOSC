#-*- coding = UTF8 -*-
'''
    file : drawSignal.py
    date : 2013-3-12
    author : qlzhangtju@gmail.com
    note : draw a data of sequence into a wave
'''

#直接从该文件目录运行此文件，需要如下语句才能顺利import
#import sys
#sys.path.append("..")

class DrawSignal():
    w = 600
    h = 400
    step = 40
    xAxis = h/2
    yAxis = step
    xScale = 2
    oldX = yAxis
    oldY = xAxis
    ids = []
    def __init__(self,win):
        self.win = win
        self.canvas = Canvas(win,width = self.w,height = self.h,bg = "grey")
        self.backGround()
        self.canvas.pack()

    def update(self,v):
        if len(self.ids) > self.w:
            self.canvas.delete(self.ids[0])
        for p in self.ids:
            self.canvas.move(p, self.xScale, 0)
        y =self.xAxis - v
        self.ids.append(self.canvas.create_line(self.oldX+self.xScale,self.oldY,self.oldX,y,fill = "red"))
        self.oldY = y

    def backGround(self):
        for i in range(0,self.h,self.step):
            self.canvas.create_line(0,i,self.w,i,width = 1.2)
        for i in range(0,self.w,self.step):
            self.canvas.create_line(i,0,i,self.h,width = 1.2)
        #画x轴
        self.canvas.create_line(0,self.xAxis,self.w,self.xAxis,width = 2)
        #画y轴
        self.canvas.create_line(self.yAxis,0,self.yAxis,self.h,width = 2)
        
    def setGeometry(self,w,h):
        pass
    def xZoom(self,ratio):
        pass
    def yZoom(self,ratio):
        pass
