import sys
# pip install pyqt6
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import pyqtSignal
from PyQt6 import QtCore
from QtGui import Ui_MainWindow
import time
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
# Khai bao code
        self.uic.startButton.clicked.connect(self.show_list)
        self.uic.clearButton.clicked.connect(self.show_clear)
        self.uic.removeButton.clicked.connect(self.show_remove)
    def show_list(self):
        self.uic.listWidget.addItem("hello")
        self.uic.listWidget.insertItem(1,"hello1")
    def show_clear(self):
        self.uic.listWidget.clear()
    def  show_remove(self):
        self.uic.listWidget.takeItem(1)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())