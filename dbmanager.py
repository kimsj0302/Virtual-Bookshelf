
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

from enum import Enum
class DBManger():
    class TARGET(Enum):
        series = 0
        books = 1
    def __init__(self):
        self.series_arr = []
        self.books_arr = []
        self.category_arr = []
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("./test.db")
        db.open()
        self.update()
        self.target_arr = self.series_arr
        self.target_info = self.TARGET.series
    def update(self):
        query = QSqlQuery()
        query.exec_("SELECT * FROM SERIES")
        self.series_arr = []
        while query.next():
            self.series_arr.append([query.value(0),query.value(1),query.value(2),query.value(3),query.value(4)])
        print(self.series_arr)
        query.exec_("SELECT * FROM BOOK")
        self.books_arr = []
        while query.next():
            self.books_arr.append([query.value(0),query.value(1),query.value(2),query.value(3)])
        print(self.books_arr)
        query.exec_("SELECT * FROM CATEGORY")
        self.category_arr = []
        while query.next():
            self.category_arr.append([query.value(0),query.value(1)])
        print(self.category_arr)
    def get_series_arr(self):
        return self.series_arr
    def get_books_arr(self):
        return self.books_arr
    def get_image(self,index):
        if self.target_info == self.TARGET.series:
            series = self.target_arr[index][0]
            for s in self.books_arr:
                if s[1]==1 and s[2]==series:
                    return s[3]
        else:
            return self.target_arr[index][3]
        return None
    def get_books_from_sereis(self,series):
        temp_arr= []
        for s in self.books_arr:
            if s[2]==series:
                temp_arr.append(s)
        return temp_arr
    def get_target_len(self):
        return len(self.target_arr)
    def get_target_image(self,series):
        return len(self.target_arr)
    def is_series_with_a_book(self,index):
        return len(self.get_books_from_sereis(self.target_arr[index][0])) == 1
    def updata_target_by_click_series(self,index):
        self.target_arr = self.get_books_from_sereis(self.target_arr[index][0])
        self.target_info = self.TARGET.books
    def is_series(self):
        return self.target_info == self.TARGET.series
    def get_title_string(self,index):
        if self.target_info == self.TARGET.series:
            return self.target_arr[index][1]
        else:
            #Will Fix
            return self.series_arr[self.target_arr[index][2]-1][1] + " " +str(self.target_arr[index][1])