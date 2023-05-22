#Transactions (Client, Service, Amount, Commission, Description).
from general import general
from services import Services
from clients import Clients
class Transactions(general):
    def __init__(self, code=0, client=None, service=None, amount=0, commission=0, description=''):
        general.__init__(self, code)
        self.setClient(client)
        self.setService(service)
        self.setAmount(amount)
        self.setCommission(commission)
        self.setDescription(description)

    def setClient(self, client):
        if isinstance(client, Clients): self.__client = client
        else: self.__client = None
    def setService(self, service):
        if isinstance(service, Services): self.__service = service
        else: self.__service = None
    def setAmount(self, amount):
        self.__amount = amount
    def setCommission(self, commission):
        self.__commission = commission
    def setDescription(self, description):
        self.__description = description

    def getClient(self):
        return self.__client
    def getClientCode(self):
        return self.__client.getCode()
    def getClientName(self):
        return self.__client.getName()
    def getClientActivity(self):
        return self.__client.getActivity()
    def getClientAddress(self):
        return self.__client.getAddress()
    def getClientPhone(self):
        return self.__client.getPhone()

    def getService(self):
        return self.__service
    def getServiceCode(self):
        return self.__service.getCode()
    def getServiceName(self):
        return self.__service.getName()
    def getServiceDescription(self):
        return self.__service.getDescription()

    def getAmount(self):
        return self.__amount
    def getCommission(self):
        return self.__commission
    def getDescription(self):
        return self.__description

    def printTransactions(self):
        if self.getClient(): clnt = self.getClient().printClients()
        else: clnt = '-'
        if self.getService(): srvc = self.getService().printServices()
        else: srvc = '-'
        return str('Клиент: ' + clnt + '\nУслуга: ' + srvc + '\nСумма = ' + str(self.getAmount()) + ' руб.\nКомиссионные = ' + str(self.getCommission()) + '%\nОписание: ' + self.getDescription())