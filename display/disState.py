#-*- coding = UTF8 -*-
'''
    file : disState.py
    date : 2013-3-12
    author : qlzhangtju@gmail.com
    note : show the sate of the application
'''

from tkinter import *

class DisState():
    W = 50
    H = 50
    R = 40
    ID = []
    def __init__(self,master):
        self.cav = Canvas(master,width = self.W,height = self.H)
        self.cav.pack()
        self.setState("stop")

    def setState(self,s):
        for i in self.ID:
            self.cav.delete(i)
        if s == "start":
            self.ID.append(self.cav.create_oval(10,10,self.W-10,self.H-10,outline='black', fill='green'))
        else:
            self.ID.append(self.cav.create_oval(10,10,self.W-10,self.H-10,outline='black', fill='red'))
