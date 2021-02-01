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
    def __init__(self,dbmanager) :
        super().__init__()
        self.dbmanager = dbmanager

        self.initUI()
        self.book_arr = [self.book1,self.book2,self.book3,self.book4,self.book5,self.book6,self.book7,self.book8,
        self.book9,self.book10,self.book11,self.book12,self.book13,self.book14,self.book15,self.book16,self.book17,self.book18]
        self.page = 1


        self.reload()
    def reload(self):
        self.paste_data()
    def paste_data(self):
        for i in range((self.page-1)*18,(self.page)*18):
            t = QPixmap()
            book_gui_index = i - (self.page-1)*18
            if i >= self.dbmanager.get_target_len():
                t.load("./empty.jpg")
            else:
                t.load(self.dbmanager.get_image(i))
            t = t.scaledToWidth(175)
            self.book_arr[book_gui_index].setPixmap(t)


    def book_clicked(self,label,n,event):
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
        
        self.title = QLabel("")

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
        self.book_grid.addWidget(self.title,1,0,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title,1,1,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title,1,2,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title,1,3,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title,1,4,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title,1,5,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title,3,0,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title,3,1,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title,3,2,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title,3,3,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title,3,4,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title,3,5,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title,5,0,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title,5,1,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title,5,2,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title,5,3,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title,5,4,alignment=Qt.AlignCenter)
        self.book_grid.addWidget(self.title,5,5,alignment=Qt.AlignCenter)



        self.setLayout(self.book_grid)
    
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
        aw = DataAddWidget(self.dbmanager)
        r = aw.showModal()
        if r:
            self.dbmanager.add_new_book(aw.get_index(),aw.get_series(),aw.get_path().replace("/","\\"))
            self.dbmanager.update()
            self.reload()
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.dbmanager = DBManger()

        self.wg = BookWidget(self.dbmanager)
        
        self.setCentralWidget(self.wg)

        self.init_menu_toolbar()

        self.init_statusbar()


        self.show()
    def init_menu_toolbar(self):
        addingAction = QAction(QIcon('./images/add.png'),'Add',self)
        addingAction.setShortcut('Ctrl+A')
        addingAction.setStatusTip('add new book')
        addingAction.triggered.connect(self.add)
        
        homeAction = QAction(QIcon('./images/home.png'),'Home',self)
        homeAction.setShortcut('Ctrl+H')
        homeAction.setStatusTip('Home')
        homeAction.triggered.connect(self.home)

        searchAction = QAction(QIcon('./images/search.png'),'Search',self)
        searchAction.setShortcut('Ctrl+S')
        searchAction.setStatusTip('Search')
        searchAction.triggered.connect(self.search)

        nextAction = QAction(QIcon('./images/next.png'),'Next Page',self)
        nextAction.setShortcut('Ctrl+X')
        nextAction.setStatusTip('next page')
        nextAction.triggered.connect(self.next)

        
        beforeAction = QAction(QIcon('./images/before.png'),'Before Page',self)
        beforeAction.setShortcut('Ctrl+Z')
        beforeAction.setStatusTip('before page')
        beforeAction.triggered.connect(self.before)


        toolbar = self.addToolBar('Add Book')
        toolbar.addAction(addingAction)
        toolbar.addAction(searchAction)
        toolbar.addAction(homeAction)
        toolbar.addAction(beforeAction)
        toolbar.addAction(nextAction)


        toolbar.setStyleSheet("background-color: white")
        toolbar.setAllowedAreas(Qt.BottomToolBarArea)
        toolbar.setMovable(False)
        toolbar.setFixedHeight(30)

    def init_statusbar(self):


        self.current_page = QLabel(" 0 / 0 ")

        statusbar = self.statusBar()
        statusbar.addPermanentWidget(self.current_page)

        statusbar.setStyleSheet("background-color: white")
    def add(self):
        self.wg.add()
    def next(self):
        return
    def before(self):
        return
    def home(self):
        self.dbmanager.init()
        self.wg.reload()
    def search(self):
        return
if __name__ == "__main__":
    app = QApplication(sys.argv)
    stylesheet = """
        QMainWindow {
            
            background-repeat: no-repeat;
        }
    """
    app.setStyleSheet(stylesheet)
    main= MainWindow()
    app.exec_()