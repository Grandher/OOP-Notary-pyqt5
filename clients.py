#Clients (Name, Activity, Address, Phone).
from general import general
class Clients(general):
    def __init__(self, code=0, name='', activity='', address='', phone=''):
        general.__init__(self, code)
        self.setName(name)
        self.setActivity(activity)
        self.setAddress(address)
        self.setPhone(phone)

    def setName(self, name):
        self.__name = name
    def setActivity(self, activity):
        self.__activity = activity
    def setAddress(self, address):
        self.__address = address
    def setPhone(self, phone):
        self.__phone = phone

    def getName(self):
        return self.__name
    def getActivity(self):
        return self.__activity
    def getAddress(self):
        return self.__address
    def getPhone(self):
        return self.__phone

    def printClients(self):
        return str(self.getName() + ', ' + self.getActivity() + ', ' + self.getAddress() + ', ' + self.getPhone())