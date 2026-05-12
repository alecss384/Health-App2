#import
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from Variables_py import Variables_py

class FinalWin(QWidget):
    def __init__(self):
        super().__init__
        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self):
        self.setWindowTitle()    

app = QApplication([])
main_win = QWidget()


main_win.setWindowTitle("Results")
main_win.resize(400,200)