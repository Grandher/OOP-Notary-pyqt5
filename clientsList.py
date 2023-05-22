from generalList import generalList
from clients import Clients

class ClientsList(generalList):
	def appendItem(self, value):
		if isinstance(value, Clients): generalList.appendItem(self, value)

	def createItem(self, code, name='', activity='', address='', phone=''):
		if code in self.getCodes():
			print(f'Клиент с кодом {code} уже существует')
		else:
			generalList.appendItem(self, Clients(code, name, activity, address, phone))
	
	def newItem(self, name='', activity='', address='', phone=''):
		generalList.appendItem(self, Clients(self.getNewCode(), name, activity, address, phone))

	def printClientsList(self):
		s = ''
		for i in self.getItems():
			s+=i.printClients() + '\n'
		return s