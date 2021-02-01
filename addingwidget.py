import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
class DataAddWidget(QDialog):
    def __init__(self,dbmanager):
        super().__init__()
        self.dbmanager = dbmanager
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Add')
        self.tabs = QTabWidget()
        self.tab1 = SeriesAddWidget(self.dbmanager)
        self.tab2 = BookAddWidget(self.dbmanager)
        self.tabs.addTab(self.tab1,"Series")
        self.tabs.addTab(self.tab2,"Book")

        

        layout = QVBoxLayout()

        layout.addWidget(self.tabs)

        btnOK = QPushButton("확인")
        btnOK.clicked.connect(self.onOKButtonClicked)
        btnCancel = QPushButton("취소")
        btnCancel.clicked.connect(self.onCancelButtonClicked)
        
        subLayout = QHBoxLayout()
        subLayout.addWidget(btnOK)
        subLayout.addWidget(btnCancel)
        layout.addLayout(subLayout)
        layout.addStretch(1)
        self.setLayout(layout)
    def onOKButtonClicked(self):
        self.accept()
    def onCancelButtonClicked(self):
        self.reject()
        
    def showModal(self):
        return super().exec_()
class SeriesAddWidget(QWidget):
    def __init__(self,dbmanager):
        super().__init__()
        self.dbmanager = dbmanager
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Add New Series')


        title_select = QHBoxLayout()
        title_label = QLabel("Title")
        self.title_line = QLineEdit(self)
        title_select.addWidget(title_label)
        title_select.addWidget(self.title_line)
        
        author_select = QHBoxLayout()
        author_label = QLabel("Author")
        self.author_line = QLineEdit(self)
        author_select.addWidget(author_label)
        author_select.addWidget(self.author_line)

        category_select = QHBoxLayout()
        category_label = QLabel("Series")
        self.category_box = QComboBox()
        for s in self.dbmanager.get_category_list():
            self.category_box.addItem(s)
        category_select.addWidget(category_label)
        category_select.addWidget(self.category_box)

        

        
        layout = QVBoxLayout()
        layout.addItem(title_select)
        layout.addItem(author_select)
        layout.addItem(category_select)

        
        layout.addStretch(1)
        self.setLayout(layout)

class BookAddWidget(QWidget):
    def __init__(self,dbmanager):
        super().__init__()
        self.dbmanager = dbmanager
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Add New Book')


        series_select = QHBoxLayout()
        series_label = QLabel("Series")
        self.series_box = QComboBox()
        for s in self.dbmanager.get_series_list():
            print(s)
            self.series_box.addItem(s)
        series_select.addWidget(series_label)
        series_select.addWidget(self.series_box)
        
        index_select = QHBoxLayout()
        index_label = QLabel("Index")
        self.index_box = QSpinBox()
        index_select.addWidget(index_label)
        index_select.addWidget(self.index_box)

        path_select = QHBoxLayout()
        path_label = QLabel("Path")
        self.path_text = QLabel()
        path_but = QPushButton('...')
        path_but.clicked.connect(self.getFilePath)
        path_select.addWidget(path_label)
        path_select.addWidget(self.path_text)
        path_select.addWidget(path_but)
        self.preview = QLabel("preview")

        

        layout = QVBoxLayout()
        
        layout_item = QVBoxLayout()
        layout_item.addItem(series_select)
        layout_item.addItem(index_select)
        layout_item.addItem(path_select)
        
        layout_body = QHBoxLayout()
        layout_body.addWidget(self.preview)
        layout_body.addItem(layout_item)

        layout.addItem(layout_body)

        layout.addStretch(1)
        self.setLayout(layout)
    def getFilePath(self):
        fname = QFileDialog.getOpenFileName(self)
        self.path_text.setText(fname[0])
        self._update_preview()
    def _update_preview(self):
        t = QPixmap()
        t.load(self.path_text.text())
        t = t.scaledToWidth(75)
        self.preview.setPixmap(t)
    def showModal(self):
        return super().exec_()
    def get_series(self):
        return self.series_box.currentIndex()+1
    def get_path(self):
        return self.path_text.text()
    def get_index(self):
        return self.index_box.value()