#-*- coding:utf-8 -*-
import json
from data import data

class datajson(data):
    def read(self):
        with open(self.getInp(),"r", encoding="utf-8") as read_file:
            data=json.load(read_file)
        for k in data.keys():
            if k=='Services':
                    for a in data[k]:
                        code, name, description=0,'',''
                        for s in a.keys():
                            if s=="Code":code=a[s]
                            if s=="Name":name=a[s]
                            if s=="Description":description=a[s]
                        self.getNotary().createService(code, name, description)
            if k=='Clients':
                for a in data[k]:
                    code, name, activity, address, phone=0,'','','',''
                    for c in a.keys():
                        if c=="Code":code=a[c]
                        if c=="Name":name=a[c]
                        if c=="Activity":activity=a[c]
                        if c=="Address":address=a[c]
                        if c=="Phone":phone=a[c]
                    self.getNotary().createClient(code, name, activity, address, phone)
            if k=='Transactions':
                for a in data[k]:
                    code, client, service, amount, commission, description=0,None,None,0,0,''
                    for t in a.keys():
                        if t=="Code":code=a[t]
                        if t=="Client":client=self.getNotary().getClient(int(a[t]))
                        if t=="Service":service=self.getNotary().getService(int(a[t]))
                        if t=="Amount":amount=a[t]
                        if t=="Commission":commission=a[t]
                        if t=="Description":description=a[t]
                    self.getNotary().createTransaction(code, client, service, amount, commission, description)
    def write(self):
        data={'Services':[],'Clients':[],'Transactions':[]}
        for c in self.getNotary().getServiceList():
            sc={}
            sc['Code']=c.getCode()
            sc['Name'] = c.getName()
            sc['Description'] = c.getDescription()
            data['Services'].append(sc)
        for c in self.getNotary().getClientList():
            cl={}
            cl["Code"] = c.getCode()
            cl['Name'] = c.getName()
            cl['Activity'] = c.getActivity()
            cl['Address'] = c.getAddress()
            cl['Phone'] = c.getPhone()
            data['Clients'].append(cl)
        for c in self.getNotary().getTransactionList():
            tr={}
            tr["Code"] = c.getCode()
            tr['Client'] = c.getClientCode()
            tr['Service'] = c.getServiceCode()
            tr['Amount'] = c.getAmount()
            tr['Commission'] = c.getCommission()
            tr['Description'] = c.getDescription()
            data['Transactions'].append(tr)
        with open(self.getOut(), "w", encoding="utf-8") as write_file:
            json.dump(data, write_file, indent=1, ensure_ascii=False)
