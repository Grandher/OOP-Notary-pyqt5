#-*- coding:utf-8 -*-
from servicesList import ServicesList
from clientsList import ClientsList
from transactionsList import TransactionsList

class Notary:
    def __init__(self):
        self.__Services = ServicesList()
        self.__Clients = ClientsList()
        self.__Transactions = TransactionsList()

    def clear(self):
        self.__Services.clear()
        self.__Clients.clear()
        self.__Transactions.clear()

    def createService(self, code, name='', description=''):
        self.__Services.createItem(code, name, description)
    def newService(self, name='', description=''):
        self.__Services.newItem(name, description)
    def removeService(self, code):
        if self.__Transactions.getItems() != []:
            for b in self.__Transactions.getItems():
                if b.getService().getCode() == code:
                    return False;
        self.__Services.removeItem(code)
        return True
    def getService(self, code):
        return self.__Services.findByCode(code)
    def getServiceList(self):
        return self.__Services.getItems()
    def getServiceCodes(self):
        return self.__Services.getCodes()



    def createClient(self, code, name='', activity='', address='', phone=''):
        self.__Clients.createItem(code, name, activity, address, phone)
    def newClient(self, name='', activity='', address='', phone=''):
        self.__Clients.newItem(name, activity, address, phone)
    def removeClient(self, code):
        if self.__Transactions.getItems() != []:
            for b in self.__Transactions.getItems():
                if b.getClient().getCode() == code:
                    return False;
        self.__Clients.removeItem(code)
        return True
    def getClient(self, code):
        return self.__Clients.findByCode(code)
    def getClientList(self):
        return self.__Clients.getItems()
    def getClientCodes(self):
        return self.__Clients.getCodes()



    def createTransaction(self, code, client=None, service=None, amount=0, commission=0, description=''):
        self.__Transactions.createItem(code, client, service, amount, commission, description)
    def newTransaction(self, client=None, service=None, amount=0, commission=0, description=''):
        self.__Transactions.newItem(client, service, amount, commission, description)
    def removeTransaction(self, code):
        self.__Transactions.removeItem(code)
    def getTransaction(self, code):
        return self.__Transactions.findByCode(code)
    def getTransactionList(self):
        return self.__Transactions.getItems()
    def getTransactionCodes(self):
        return self.__Transactions.getCodes()