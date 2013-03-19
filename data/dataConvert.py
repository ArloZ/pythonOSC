#-*- coding = UTF8 -*-
'''
    file : dataConvert.py
    date : 2013-3-12
    author : qlzhangtju@gmail.com
    note : convert the value the display available
'''

class DataConvert():
    '''
    brief 将数值转换成电压表示形式,转换后单位为 V(伏特)
    bits 量化精度
    posV 正向电压
    negV 反向电压
    '''
    def __init__(self,bits = 8,posV = 1,negV = 0):
        self.bits = bits
        self.negV = negV
        self.posV = posV
        self.delta = (posV - negV)/((1 << bits)-1)
        

    def setFormat(self,bits = 8,posV = 1,negV = 0):
        self.bits = bits
        self.negV = negV
        self.posV = posV
        self.delta = (posV - negV)/((1 << bits)-1)

    def convert(self,data):
        print("delta:",self.delta)
        val = self.delta * data
        return val 
