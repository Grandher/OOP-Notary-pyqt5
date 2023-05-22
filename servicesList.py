from generalList import generalList
from services import Services

class ServicesList(generalList):
	def appendItem(self, value):
		if isinstance(value, Services): generalList.appendItem(self, value)

	def createItem(self, code, name='', description=''):
		if code in self.getCodes():
			print(f'Услуга с кодом {code} уже существует')
		else:
			generalList.appendItem(self, Services(code, name, description))
	
	def newItem(self, name='', description=''):
		generalList.appendItem(self, Services(self.getNewCode(), name, description))

	def printServicesList(self):
		s = ''
		for i in self.getItems():
			s+=i.printServices() + '\n'
		return s