#Services (Name, Description)
from general import general
class Services(general):
    def __init__(self, code=0, name='', description=''):
        general.__init__(self, code)
        self.setName(name)
        self.setDescription(description)

    def setName(self, name):
        self.__name = name
    def setDescription(self, description):
        self.__description = description

    def getName(self):
        return self.__name
    def getDescription(self):
        return self.__description

    def printServices(self):
        return str(self.getName() + ', ' + self.getDescription())