import sys
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtCore import *
from enum import Enum

import functools
import subprocess

from searchwidget import *
from addingwidget import *
from dbmanager import *


class BookWidget(QWidget):
    
    class TARGET(Enum):
        series = 0
        books = 1
    def __init__(self) :
        super().__init__()
        
        self.dbmanager = DBManger()

        self.initUI()
        self.book_arr = [self.book1,self.book2,self.book3,self.book4,self.book5,self.book6,self.book7,self.book8,
        self.book9,self.book10,self.book11,self.book12,self.book13,self.book14,self.book15,self.book16,self.book17,self.book18]
        self.title_arr = [self.title1,self.title2,self.title3,self.title4,self.title5,self.title6,self.title7,self.title8,
        self.title9,self.title10,self.title11,self.title12,self.title13,self.title14,self.title15,self.title16,self.title17,self.title18]
        self.page = 1


        self.reload()



        '''
        self.bg  = QPixmap()
        self.bg.load("bg.jpg")
        self.bg  = self.bg.scaledToWidth(496)
        self.background.setPixmap(self.bg)
        '''
        #self.addb1(150)
    def reload(self):
        self.paste_data()
    def paste_data(self):
        for i in range((self.page-1)*18,(self.page)*18):
            print(i)
            t = QPixmap()
            book_gui_index = i - (self.page-1)*18
            if i >= self.dbmanager.get_target_len():
                t.load("./empty.jpg")
                self.title_arr[book_gui_index].setText("")
            else:
                t.load(self.dbmanager.get_image(i))
                self.title_arr[book_gui_index].setText(self.dbmanager.get_title_string(i))
            t = t.scaledToWidth(200)
            self.book_arr[book_gui_index].setPixmap(t)


    def book_clicked(self,label,n,event):
        print((self.page-1)*18 + n)
        if (self.page-1)*18 + n < self.dbmanager.get_target_len():
            if self.dbmanager.is_series():
                if self.dbmanager.is_series_with_a_book((self.page-1)*18 + n):
                    subprocess.run(['C:\Program Files\Honeyview\Honeyview.exe',self.dbmanager.get_image((self.page-1)*18 + n)])
                else:
                    self.dbmanager.updata_target_by_click_series((self.page-1)*18 + n)
                    self.reload()
            else:
                subprocess.run(['C:\Program Files\Honeyview\Honeyview.exe',self.dbmanager.get_image((self.page-1)*18 + n)])
    def initUI(self):

        self.book_grid = QGridLayout()
        self.book1 = QLabel("0")
        self.book2 = QLabel("1")
        self.book3 = QLabel("2")
        self.book4 = QLabel("3")
        self.book5 = QLabel("4")
        self.book6 = QLabel("5")
        self.book7 = QLabel("6")
        self.book8 = QLabel("7")
        self.book9 = QLabel("8")
        self.book10 = QLabel("9")
        self.book11 = QLabel("10")
        self.book12 = QLabel("11")
        self.book13 = QLabel("12")
        self.book14 = QLabel("13")
        self.book15 = QLabel("14")
        self.book16 = QLabel("15")
        self.book17 = QLabel("16")
        self.book18 = QLabel("17")
        
        self.title1 = QLabel("t0")
        self.title2 = QLabel("t1")
        self.title3 = QLabel("t2")
        self.title4 = QLabel("t3")
        self.title5 = QLabel("t4")
        self.title6 = QLabel("t5")
        self.title7 = QLabel("t6")
        self.title8 = QLabel("t7")
        self.title9 = QLabel("t8")
        self.title10 = QLabel("t9")
        self.title11 = QLabel("t10")
        self.title12 = QLabel("t11")
        self.title13 = QLabel("t12")
        self.title14 = QLabel("t13")
        self.title15 = QLabel("t14")
        self.title16 = QLabel("t15")
        self.title17 = QLabel("t16")
        self.title18 = QLabel("t17")

        self.book1.mousePressEvent = functools.partial(self.book_clicked,self.book1,0)
        self.book2.mousePressEvent = functools.partial(self.book_clicked,self.book2,1)
        self.book3.mousePressEvent = functools.partial(self.book_clicked,self.book3,2)
        self.book4.mousePressEvent = functools.partial(self.book_clicked,self.book4,3)
        self.book5.mousePressEvent = functools.partial(self.book_clicked,self.book5,4)
        self.book6.mousePressEvent = functools.partial(self.book_clicked,self.book6,5)
        self.book7.mousePressEvent = functools.partial(self.book_clicked,self.book7,6)
        self.book8.mousePressEvent = functools.partial(self.book_clicked,self.book8,7)
        self.book9.mousePressEvent = functools.partial(self.book_clicked,self.book9,8)
        self.book10.mousePressEvent = functools.partial(self.book_clicked,self.book10,9)
        self.book11.mousePressEvent = functools.partial(self.book_clicked,self.book11,10)
        self.book12.mousePressEvent = functools.partial(self.book_clicked,self.book12,11)
        self.book13.mousePressEvent = functools.partial(self.book_clicked,self.book13,12)
        self.book14.mousePressEvent = functools.partial(self.book_clicked,self.book14,13)
        self.book15.mousePressEvent = functools.partial(self.book_clicked,self.book15,14)
        self.book16.mousePressEvent = functools.partial(self.book_clicked,self.book16,15)
        self.book17.mousePressEvent = functools.partial(self.book_clicked,self.book17,16)
        self.book18.mousePressEvent = functools.partial(self.book_clicked,self.book18,17)
        self.book_grid.addWidget(self.book1,0,0,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.book2,0,1,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.book3,0,2,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.book4,0,3,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.book5,0,4,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.book6,0,5,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.book7,2,0,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.book8,2,1,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.book9,2,2,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.book10,2,3,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.book11,2,4,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.book12,2,5,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.book13,4,0,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.book14,4,1,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.book15,4,2,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.book16,4,3,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.book17,4,4,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.book18,4,5,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title1,1,0,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title2,1,1,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title3,1,2,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title4,1,3,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title5,1,4,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title6,1,5,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title7,3,0,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title8,3,1,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title9,3,2,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title10,3,3,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title11,3,4,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title12,3,5,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title13,5,0,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title14,5,1,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title15,5,2,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title16,5,3,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title17,5,4,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title18,5,5,alignment=Qt.AlignCenter)



        self.setLayout(self.book_grid)
    def resizeEvent(self, event):
        print("resize")
        print(self.frameGeometry().width())
        #self.addb1(180)
        print(self.frameGeometry().height())
        QWidget.resizeEvent(self, event)
    def addb1(self,w):   
        self.b1  = QPixmap()
        self.b1.load("img.jpg")
        self.b1  = self.b1.scaledToWidth(w)
        self.book1.setPixmap(self.b1)
        self.book2.setPixmap(self.b1)
        self.book3.setPixmap(self.b1)
        self.book4.setPixmap(self.b1)
        self.book5.setPixmap(self.b1)
        self.book6.setPixmap(self.b1)
        self.book7.setPixmap(self.b1)
        self.book8.setPixmap(self.b1)
        self.book9.setPixmap(self.b1)
        self.book10.setPixmap(self.b1)
        self.book11.setPixmap(self.b1)
        self.book12.setPixmap(self.b1)
        self.book13.setPixmap(self.b1)
        self.book14.setPixmap(self.b1)
        self.book15.setPixmap(self.b1)
        self.book16.setPixmap(self.b1)
        self.book17.setPixmap(self.b1)
        self.book18.setPixmap(self.b1)


class MainWidget(QWidget):
    class VIEW(Enum):
        Thumbnail = 0
        List = 1
    def __init__(self) :
        super().__init__()
        grid = QGridLayout()
        self.bookwidget = BookWidget()
        


        self.home_dir = QPushButton(">",self)
        self.home_dir.setIcon(QIcon('./images/home.png'))

        self.dir_path = QHBoxLayout()
        self.dir_path.addWidget(self.home_dir)

        self.view_butt = QPushButton("",self)
        self.view_butt.setFixedSize(30,30)
        self.view_butt.clicked.connect(self.view_switch)
        self._set_thumbnail_view()
        
        self.next_butt = QPushButton("",self)
        self.next_butt.setFixedSize(30,30)
        self.before_butt = QPushButton("",self)
        self.before_butt.setFixedSize(30,30)
        self.next_butt.setIcon(QIcon('./images/next.png'))
        self.before_butt.setIcon(QIcon('./images/before.png'))

        self.search_butt = QPushButton("",self)
        self.search_butt.setFixedSize(30,30)
        self.search_butt.setIcon(QIcon('./images/search.png'))
        self.search_butt.clicked.connect(self.search)

        self.add_butt = QPushButton("",self)
        self.add_butt.setFixedSize(30,30)
        self.add_butt.setIcon(QIcon('./images/add.png'))
        self.add_butt.clicked.connect(self.add)

        self.current_page = QLabel(" 0 / 0 ")
        

        viewline = QHBoxLayout()
        viewline.addWidget(self.add_butt)
        viewline.addWidget(self.search_butt)
        viewline.addWidget(self.view_butt)
        viewline.addWidget(self.before_butt)
        viewline.addWidget(self.current_page)
        viewline.addWidget(self.next_butt)

        grid.addItem(self.dir_path,0,0,alignment=Qt.AlignLeft)
        grid.addWidget(self.bookwidget,1,0)
        grid.addItem(viewline,2,0,alignment=Qt.AlignRight)
        self.setLayout(grid)
    def _set_list_view(self):
        self.view_butt.setIcon(QIcon('./images/list.png'))
        self.view_state = self.VIEW.List
        self.view_butt.setToolTip('Switch to thumbnail view')  
        # call function to swtich list view
    def _set_thumbnail_view(self):
        self.view_butt.setIcon(QIcon('./images/thumbnail.png'))
        self.view_state = self.VIEW.Thumbnail
        self.view_butt.setToolTip('Switch to list view')  
        # call function to swtich thumbnail view
    def view_switch(self):
        if self.view_state == self.VIEW.Thumbnail:
            self._set_list_view()
        else:
            self._set_thumbnail_view()
    def search(self):
        self.sw = SearchWidget()
        self.sw.show()
    def add(self):
        self.aw = AddingWidget()
        self.aw.show()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        wg = MainWidget()
        
        self.setCentralWidget(wg)

        
        '''
        Menu bar
        '''
        menubar = self.menuBar()
        menu = QMenu('File', self)
        menubar.addMenu(menu)
        self.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main= MainWindow()
    app.exec_()