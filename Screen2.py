from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout , QLineEdit
from Variables import *

class Screen2(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(W1_window_name)
        self.resize(win_width,win_height)
        self.move(win_move_x,win_move_y)
    def initUI(self):
        self.h_line =QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.label_name = QLabel("label_name")
        self.label_name.setText(W2_name)
        self.r_line.addWidget(self.label_name)
        
    def connects(self):
        pass
        
            

app = QApplication([])

mw = Screen2()
app.exec_()