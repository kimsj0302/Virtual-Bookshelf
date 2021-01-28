import sys
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("test.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.initUI()
        '''
        self.bg  = QPixmap()
        self.bg.load("bg.jpg")
        self.bg  = self.bg.scaledToWidth(496)
        self.background.setPixmap(self.bg)
        '''
        self.addb1(self.frameGeometry().width()/100)
    def initUI(self):
        
        #but = QPushButton()
        #self.gridLayout.addWidget(but,0,0)

        self.book_grid = QGridLayout()
        self.book1 = QLabel("book1")
        self.book2 = QLabel("book2")
        self.book3 = QLabel("book3")
        self.book4 = QLabel("book4")
        self.book5 = QLabel("book5")
        self.book6 = QLabel("book6")
        self.book7 = QLabel("book7")
        self.book8 = QLabel("book8")
        self.book9 = QLabel("book9")
        self.book10 = QLabel("book10")
        self.book11 = QLabel("book11")
        self.book12 = QLabel("book12")
        self.book13 = QLabel("book13")
        self.book14 = QLabel("book14")
        self.book15 = QLabel("book15")
        self.book16 = QLabel("book16")
        self.book17 = QLabel("book17")
        self.book18 = QLabel("book18")
        self.book_grid.addWidget(self.book1,0,0)
        '''
        self.book_grid.addWidget(self.book2,0,1)
        self.book_grid.addWidget(self.book3,0,2)
        self.book_grid.addWidget(self.book4,0,3)
        self.book_grid.addWidget(self.book5,0,4)
        self.book_grid.addWidget(self.book6,0,5)
        self.book_grid.addWidget(self.book7,1,0)
        self.book_grid.addWidget(self.book8,1,1)
        self.book_grid.addWidget(self.book9,1,2)
        self.book_grid.addWidget(self.book10,1,3)
        self.book_grid.addWidget(self.book11,1,4)
        self.book_grid.addWidget(self.book12,1,5)
        self.book_grid.addWidget(self.book13,2,0)
        self.book_grid.addWidget(self.book14,2,1)
        self.book_grid.addWidget(self.book15,2,2)
        self.book_grid.addWidget(self.book16,2,3)
        self.book_grid.addWidget(self.book17,2,4)
        self.book_grid.addWidget(self.book18,2,5)
        '''
        #self.gridLayout.addItem(self.book_grid,0,0)
        self.gridLayout.addWidget(self.book1,0,0)
        self.gridLayout.addWidget(self.book2,0,1)
        self.gridLayout.addWidget(self.book3,0,2)
        self.show()
    def resizeEvent(self, event):
        print("resize")
        print(self.frameGeometry().width())
        self.addb1(self.frameGeometry().width()/10)
        print(self.frameGeometry().height())
        QWidget.resizeEvent(self, event)
    def addb1(self,w):   
        self.b1  = QPixmap()
        self.b1.load("book1.jpg")
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
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()