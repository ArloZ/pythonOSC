#-*- coding= UTF8 -*-
'''
    file : commuart.py
    date : 2013-3-12
    author : qlzhangtju@gmail.com
    note : capture data from uart
'''

from serial import *

class CommUart():
    def __init__(self,Port = 0,BaudRate = 9600):
        try:
            self.ser = Serial(Port)
            if not self.ser.isOpen(): 
                self.ser.open()
            self.ser.write(20)
            self.ser.close()
        except Exception as err:
            print(err)

    def send(self,data):
        self.ser.write(data)
    def receive(self):
        pass
