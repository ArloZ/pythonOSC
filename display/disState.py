#-*- coding = UTF8 -*-
'''
    file : disState.py
    date : 2013-3-12
    author : qlzhangtju@gmail.com
    note : show the sate of the application
'''

class disState():
    W = 50
    H = 50
    R = 40
    ID = []
    def __init__(self,master):
        self.cav = Canvas(master,width = W,height = H)
        self.cav.pack()
        self.setState("stop")

    def setState(self,s):
        if ID[0]:
            self.cav.delete(ID[0])
        if s == "start":
            ID.append(self.cav.create_oval(0,0,self.W,self.H,outline='black', fill='green'))
        else:
            ID.append(self.cav.create_oval(0,0,self.W,self.H,outline='black', fill='red'))
