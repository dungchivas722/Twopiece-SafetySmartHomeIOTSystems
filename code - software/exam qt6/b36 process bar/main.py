import sys
# pip install pyqt6
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import pyqtSignal, QTimer
from PyQt6 import QtCore
from QtGui import Ui_MainWindow
import time
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
# Khai bao code
        self.uic.progressBar.setValue(0)
        self.uic.startButton.clicked.connect(self.program)
        self.a = 0
    def program(self):
        timer = QTimer(self)
        timer.timeout.connect(self.process)
        timer.start(100)
    def process(self):
        self.a += 1
        self.uic.progressBar.setValue(self.a)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())