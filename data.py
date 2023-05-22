#-*- coding:utf-8 -*-
class data:
    def __init__(self, notary=None,inp='',out=''):
        self.setNotary(notary)
        self.setInp(inp)
        self.setOut(out)
    def setNotary(self,value): self.__notary=value
    def setInp(self,value): self.__inp=value
    def setOut(self,value): self.__out=value
    def getNotary(self): return self.__notary
    def getInp(self): return self.__inp
    def getOut(self): return self.__out

    def readFile(self,filename):
        self.setInp(filename)
        self.read()
    def writeFile(self,filename):
        self.setOut(filename)
        self.write()
    def read(self): pass
    def write(self): pass

