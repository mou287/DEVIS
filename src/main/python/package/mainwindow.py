from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow

class MainWindow(QtWidgets.QDialog):

    def __init__(self, ctx):
        super().__init__()
        self.ctx = ctx
        self.main_layout = QtWidgets.QHBoxLayout()
        self.btn_click_me = QtWidgets.QPushButton("click me ..")
        self.main_layout.addWidget(self.btn_click_me)
        self.setLayout(self.main_layout)
        self.btn_click_me.clicked.connect(self.on_click_me)

    def on_click_me(self):
        print("click me")

