#-*- coding:utf-8 -*-
import os
import sqlite3 as db
from data import data
emptydb = """
PRAGMA foreign_keys = ON;

CREATE TABLE Services (
    Code            INTEGER PRIMARY KEY,
    Name            VARCHAR,
    Description     TEXT
);

CREATE TABLE Clients (
    Code        INT     PRIMARY KEY,
    Name        VARCHAR,
    Activity    VARCHAR,
    Address     VARCHAR,
    Phone       VARCHAR
);

CREATE TABLE Transactions (
    Code                INT        PRIMARY KEY,
    Client              INT        REFERENCES Clients (Code) ON DELETE SET NULL ON UPDATE CASCADE,
    Service             INT        REFERENCES Services (Code) ON DELETE SET NULL ON UPDATE CASCADE,
    Amount              DOUBLE,
    Commission          INT,
    Description         TEXT
);
 """

class datasql(data):
    def read(self):
        conn= db.connect(self.getInp())
        curs= conn.cursor()
        curs.execute('SELECT * FROM Services')
        data=curs.fetchall()
        for r in data: self.getNotary().createService(r[0], r[1], r[2])
        curs.execute('SELECT * FROM Clients')
        data=curs.fetchall()
        for r in data: self.getNotary().createClient(r[0], r[1], r[2], r[3], r[4])
        curs.execute('SELECT * FROM Transactions')
        data=curs.fetchall()
        for r in data:
            if r[1]: cl = int(r[1])
            else: cl = r[1]
            if r[2]: sc = int(r[2])
            else: sc = r[2]
            self.getNotary().createTransaction(r[0], self.getNotary().getClient(cl), self.getNotary().getService(sc), r[3], r[4], r[5])
        conn.close()
    def write(self):
        conn=db.connect(self.getOut())
        curs=conn.cursor()
        curs.executescript(emptydb)
        for c in self.getNotary().getServiceList():
            curs.execute("INSERT INTO Services VALUES (?, ?, ?)",\
                         ( c.getCode(),c.getName(),c.getDescription() ))
        for c in self.getNotary().getClientList():
            curs.execute("INSERT INTO Clients VALUES(?, ?, ?, ?, ?)",\
                ( c.getCode(),c.getName(),c.getActivity(),c.getAddress(),c.getPhone() ))
        for c in self.getNotary().getTransactionList():
            if c.getClient(): cl = c.getClientCode()
            else: cl = "NULL"
            if c.getService(): sc = c.getServiceCode()
            else: sc = "NULL"
            curs.execute("INSERT INTO Transactions VALUES(?, ?, ?, ?, ?, ?)",\
                ( c.getCode(),cl,sc,c.getAmount(),c.getCommission(),c.getDescription() ))    
        conn.commit()
        conn.close()
