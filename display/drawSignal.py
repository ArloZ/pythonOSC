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

from tkinter import *
from data.dataBuf import *

class DrawSignal():
    def __init__(self,win,buf = '',size = 0,w = 600,h = 400):
        self.win = win
        self.buf = buf
        self.bufsize = size
        self.width = w
        self.height = h
        self.canvas = Canvas(win,)

    def update(self):
        pass
    def setBuffer(self,buf,size):
        pass
    def setGeometry(self,w,h):
        pass
    def xZoom(self,ratio):
        pass
    def yZoom(self,ratio):
        pass
    def backGround(self):
        pass
        
