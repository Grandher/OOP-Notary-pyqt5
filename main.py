from PyQt5 import QtCore, QtGui, QtWidgets
from notary import Notary
from datajson import datajson
from datasql import datasql
from MainWindow import Ui_Notary
import os
import sys

class MyWindow(QtWidgets.QMainWindow, Ui_Notary):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.cwd = os.getcwd()

		self.clients_table.clicked.connect(self.cur_clnt)
		self.services_table.clicked.connect(self.cur_srvc)
		self.transactions_table.clicked.connect(self.cur_trans)

		self.clients_add.clicked.connect(self.add_clnt)
		self.clients_edit.clicked.connect(self.edit_clnt)
		self.clients_del.clicked.connect(self.del_clnt)

		self.services_add.clicked.connect(self.add_srvc)
		self.services_edit.clicked.connect(self.edit_srvc)
		self.services_del.clicked.connect(self.del_srvc)

		self.transactions_add.clicked.connect(self.add_trans)
		self.transactions_edit.clicked.connect(self.edit_trans)
		self.transactions_del.clicked.connect(self.del_trans)

		self.create.triggered.connect(self.new_notary)
		self.open.triggered.connect(self.open_notary)
		self.save_json.triggered.connect(self.savejson)
		self.save_sql.triggered.connect(self.savesqlite)

		self.current_client = None
		self.current_service = None
		self.current_transer = None

		self.notary = Notary()
		self.current_json = datajson()
		self.current_sqlite = datasql()

		if os.path.isfile("old.json"):
			self.open_notary("old.json")

	def combo_clnt(self):
		self.client_edit.clear()
		for i in self.notary.getClientList():
			self.client_edit
			self.client_edit.addItem(i.getName())
	def combo_srvc(self):
		self.service_edit.clear()
		for i in self.notary.getServiceList():
			self.service_edit.addItem(i.getName())

	def cur_clnt(self):
		rowPosition = self.clients_table.currentRow()
		code = self.clients_table.item(rowPosition, 0).text()
		self.current_client = self.notary.getClient(int(code))
		self.client_title_edit.setText(self.current_client.getName())
		self.activity_edit.setText(self.current_client.getActivity())
		self.address_edit.setText(self.current_client.getAddress())
		self.phone_edit.setText(self.current_client.getPhone())

	def cur_srvc(self):
		rowPosition = self.services_table.currentRow()
		code = self.services_table.item(rowPosition, 0).text()
		self.current_service = self.notary.getService(int(code))
		self.service_title_edit.setText(self.current_service.getName())
		self.description_edit.setText(self.current_service.getDescription())

	def cur_trans(self):
		rowPosition = self.transactions_table.currentRow()
		code = self.transactions_table.item(rowPosition, 0).text()
		self.current_transer = self.notary.getTransaction(int(code))
		self.client_edit.setCurrentText(self.current_transer.getClientName())
		self.service_edit.setCurrentText(self.current_transer.getServiceName())
		self.amount_edit.setText(str(self.current_transer.getAmount()))
		self.commission_edit.setText(str(self.current_transer.getCommission()))
		self.transdesc_edit.setText(self.current_transer.getDescription())

	def add_clnt(self):
		client = self.client_title_edit.text() or ""
		activity = self.activity_edit.text() or ""
		address = self.address_edit.text() or ""
		phone = self.phone_edit.text() or ""
		self.notary.newClient(client, activity, address, phone)
		self.client_title_edit.setText("")
		self.activity_edit.setText("")
		self.address_edit.setText("")
		self.phone_edit.setText("")
		self.table_render()

	def edit_clnt(self):
		if self.current_client:
			self.current_client.setName(self.client_title_edit.text())
			self.current_client.setActivity(self.activity_edit.text())
			self.current_client.setAddress(self.address_edit.text())
			self.current_client.setPhone(self.phone_edit.text())

			self.client_title_edit.setText("")
			self.activity_edit.setText("")
			self.address_edit.setText("")
			self.phone_edit.setText("")
			self.current_client = None
			self.table_render()

	def add_srvc(self):
		title = self.service_title_edit.text() or ""
		description = self.description_edit.text() or ""
		self.notary.newService(title, description)
		self.service_title_edit.setText("")
		self.description_edit.setText("")
		self.table_render()

	def edit_srvc(self):
		if self.current_service:
			self.current_service.setName(self.service_title_edit.text())
			self.current_service.setDescription(self.description_edit.text())

			self.service_title_edit.setText("")
			self.description_edit.setText("")
			self.current_service = None
			self.table_render()

	def add_trans(self):
		if len(self.notary.getClientCodes()) != 0 and len(self.notary.getServiceCodes()) != 0:
			client, service = None,None
			for i in self.notary.getClientList():
				if i.getName() == self.client_edit.currentText():
					client = i
					break
			for i in self.notary.getServiceList():
				if i.getName() == self.service_edit.currentText():
					service = i
					break
			amount = int(self.amount_edit.text()) or 0
			commission = int(self.commission_edit.text()) or 0
			transdesc = self.transdesc_edit.text() or ""
			self.notary.newTransaction(client, service, amount, commission, transdesc)
			self.amount_edit.setText("")
			self.commission_edit.setText("")
			self.transdesc_edit.setText("")
			self.table_render()
		else:
			self.message_window("Нет данных о клиентах или услугах")

	def edit_trans(self):
		if self.current_transer:
			for i in self.notary.getClientList():
				if i.getName() == self.client_edit.currentText():
					client = i
					break
			for i in self.notary.getServiceList():
				if i.getName() == self.service_edit.currentText():
					service = i
					break
			self.current_transer.setClient(client)
			self.current_transer.setService(service)
			self.current_transer.setAmount(self.amount_edit.text())
			self.current_transer.setCommission(self.commission_edit.text())
			self.current_transer.setDescription(self.transdesc_edit.text())
			self.current_transer = None
			self.table_render()

	def del_clnt(self):
		rowPosition = self.clients_table.currentRow()
		if self.current_client:
			msg = self.message_window("Удалить выбранного клиента?")
			if msg.exec_() == QtWidgets.QMessageBox.Ok:
				if self.notary.removeClient(self.current_client.getCode()):
					self.clients_table.removeRow(rowPosition)
					self.current_client = None
					self.combo_clnt()
				else: self.error_window("Данный клиент имеет активные сделки и не может быть удалён")

	def del_srvc(self):
		rowPosition = self.services_table.currentRow()
		if self.current_service:
			msg = self.message_window("Удалить выбранную услугу?")
			if msg.exec_() == QtWidgets.QMessageBox.Ok:
				if self.notary.removeService(self.current_service.getCode()):
					self.services_table.removeRow(rowPosition)
					self.current_service = None
					self.combo_srvc()
				else: self.error_window("Данная услуга находится в списке сделок и не может быть удалена")

	def del_trans(self):
		rowPosition = self.transactions_table.currentRow()
		if self.current_transer:
			msg = self.message_window("Удалить выбранную сделку?")
			if msg.exec_() == QtWidgets.QMessageBox.Ok:
				self.transactions_table.removeRow(rowPosition)
				self.notary.removeTransaction(self.current_transer.getCode())
				self.current_transer = None

	def table_render(self):
		self.transactions_table.setRowCount(0)
		self.services_table.setRowCount(0)
		self.clients_table.setRowCount(0)
		for i in self.notary.getClientList():
			rowPosition = self.clients_table.rowCount()
			self.clients_table.insertRow(rowPosition)
			self.clients_table.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(str(i.getCode())))
			self.clients_table.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(i.getName()))
			self.clients_table.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(i.getActivity()))
			self.clients_table.setItem(rowPosition , 3, QtWidgets.QTableWidgetItem(i.getAddress()))
			self.clients_table.setItem(rowPosition , 4, QtWidgets.QTableWidgetItem(i.getPhone()))

		for i in self.notary.getServiceList():
			rowPosition = self.services_table.rowCount()
			self.services_table.insertRow(rowPosition)
			self.services_table.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(str(i.getCode())))
			self.services_table.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(i.getName()))
			self.services_table.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(i.getDescription()))

		for i in self.notary.getTransactionList():
			rowPosition = self.transactions_table.rowCount()
			self.transactions_table.insertRow(rowPosition)
			self.transactions_table.setItem(rowPosition , 0, QtWidgets.QTableWidgetItem(str(i.getCode())))
			self.transactions_table.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(i.getClientName()))
			self.transactions_table.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(i.getServiceName()))
			self.transactions_table.setItem(rowPosition , 3, QtWidgets.QTableWidgetItem(str(i.getAmount())))
			self.transactions_table.setItem(rowPosition , 4, QtWidgets.QTableWidgetItem(str(i.getCommission())))
			self.transactions_table.setItem(rowPosition , 5, QtWidgets.QTableWidgetItem(i.getDescription()))
		self.combo_clnt()
		self.combo_srvc()
		self.clients_table.resizeColumnsToContents()
		self.services_table.resizeColumnsToContents()
		self.transactions_table.resizeColumnsToContents()

	def open_notary(self, path=''):
		if path:
			fileName = path
			filetype = "JSON files (*.json)"
		else:
			fileName, filetype = QtWidgets.QFileDialog.getOpenFileName(self, "Выбрать файл", \
			self.cwd, "JSON files (*.json);;SQLite files (*.sqlite)")
		if fileName != "":
			self.notary = Notary()
			if filetype == "JSON files (*.json)":
				self.current_json = datajson(self.notary, fileName, fileName)
				self.current_json.read()
			else:
				self.current_sqlite = datasql(self.notary, fileName, fileName)
				self.current_sqlite.read()
			self.table_render()

	def new_notary(self):
		msg = self.message_window("Текущие данные будут потеряны\nПродолжить?")
		if msg.exec_() == QtWidgets.QMessageBox.Ok:
			self.notary = Notary()
			self.current_json = datajson()
			self.current_sqlite = datasql()

			self.transactions_table.setRowCount(0)
			self.services_table.setRowCount(0)
			self.clients_table.setRowCount(0)
			self.combo_clnt()
			self.combo_srvc()

	def savejson(self):
		if self.current_json.getOut() != "":
			self.current_json.write()
		else:
			fileName, filetype = QtWidgets.QFileDialog.getSaveFileName(self, "Создать файл", self.cwd, "JSON files (*.json)")
			if fileName != "":
				self.current_json = datajson(self.notary, fileName, fileName)
				self.current_json.write()

	def savesqlite(self):
		if self.current_sqlite.getOut() != "":
			self.current_sqlite.write()
		else:
			fileName, filetype = QtWidgets.QFileDialog.getSaveFileName(self, "Создать файл", self.cwd, "SQLite files (*.sqlite)")
			if fileName != "":
				self.current_sqlite = datasql(self.notary, fileName, fileName)
				self.current_sqlite.write()

	def error_window(self, str):
		error = QtWidgets.QMessageBox()
		error.setWindowTitle("Ошибка")
		error.setText(str)
		error.setIcon(QtWidgets.QMessageBox.Warning)
		error.setStandardButtons(QtWidgets.QMessageBox.Ok)
		error.exec_()

	def message_window(self, str):
		error = QtWidgets.QMessageBox()
		error.setWindowTitle("Предупреждение")
		error.setText(str)
		error.setIcon(QtWidgets.QMessageBox.Information)
		error.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
		return error

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle("Нотариальная контора")
window.show()
sys.exit(app.exec_())
