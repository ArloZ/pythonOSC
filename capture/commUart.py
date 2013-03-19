#-*- coding= UTF8 -*-
'''
    file : commuart.py
    date : 2013-3-12
    author : qlzhangtju@gmail.com
    note : capture data from uart
'''

from serial import *
import threading

class CommUart(threading.Thread):
    def __init__(self,Port = 0,BaudRate = 9600):
        threading.Thread.__init__(self)
        self.thread_stop = False
        self.ser = Serial(Port,BaudRate)
        self.recCbk = None
        self.recNum = 1

    def run(self):
        while not self.thread_stop:
            if self.ser.inWaiting() == self.recNum:
                self.recCbk()
            pass

    def stop(self):
        self.thread_stop = True

    #设置接收到num个字节后的回调函数
    def setRecCbk(self,recCbk = None,num = 1):
        if not recCbk:
            print("set RecCbk failed!")
            return
        self.recCbk = recCbk
        self.recNum = num
       
    #将int数据转换成16进制发送
    def sendHex(self,data):
        try: 
            if not self.ser.isOpen(): 
                self.ser.open()
        except Exception as err:
            print(err)
        self.ser.write(chr(data).encode('utf-8'))

    #发送字符串
    def sendStr(self,strs):
        try: 
            if not self.ser.isOpen(): 
                self.ser.open()
        except Exception as err:
            print(err)
        self.ser.write(strs.encode('utf-8'))
        
    def receive(self):
        return self.ser.read(self.recNum)

