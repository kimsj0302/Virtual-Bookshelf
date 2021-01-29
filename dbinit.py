import sys
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtCore import *

app = QApplication(sys.argv)
db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("./test.db")
if db.open():
    print("open DB success.")
    query = QSqlQuery()
    query.exec_("create table person(id int primary key, name varchar(20), address varchar(30))")
    query.exec_("insert into person values(1, 'Bauer', 'beijing')")
    query.exec_("insert into person values(2, 'Jack', 'shanghai')")
    query.exec_("insert into person values(3, 'Alex', 'chengdu')")
