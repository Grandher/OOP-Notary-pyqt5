from generalList import generalList
from transactions import Transactions

class TransactionsList(generalList):
	def appendItem(self, value):
		if isinstance(value, Transactions): generalList.appendItem(self, value)

	def createItem(self, code, client=None, service=None, amount=0, commission=0, description=''):
		if code in self.getCodes():
			print(f'Сделка с кодом {code} уже существует')
		else:
			generalList.appendItem(self, Transactions(code, client, service, amount, commission, description))
	
	def newItem(self, client=None, service=None, amount=0, commission=0, description=''):
		generalList.appendItem(self, Transactions(self.getNewCode(), client, service, amount, commission, description))

	def printTransactionsList(self):
		s = ''
		for i in self.getItems():
			s+=i.printTransactions() + '\n'
		return s