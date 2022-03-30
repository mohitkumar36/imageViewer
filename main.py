from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys

class UI(QMainWindow):
    def __init__(self) -> None:
        super(UI, self).__init__()

        #load ui file
        uic.loadUi(".\\image.ui", self)

        #define our widgets
        self.button = self.findChild(QPushButton, "pushButton")
        self.label = self.findChild(QLabel, "label")

        #click dropdown Box
        self.button.clicked.connect(self.clicker)

        #show the app
        self.show()
    
    def clicker(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", "C:\\Users", "All Files (*);; PNG Files (*.png);; Jpg Files (*.jpg)")

        self.pixmap = QPixmap(fname[0])
        self.label.setPixmap(self.pixmap)


app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()