
from PyQt5.QtWidgets import *
class SearchWidget(QWidget):
    def __init__(self) :
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("TEMP")
        layout.addWidget(self.label)
        self.setLayout(layout)
    