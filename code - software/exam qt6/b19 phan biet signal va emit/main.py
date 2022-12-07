import sys
# pip install pyqt6
from PyQt6.QtWidgets import QApplication, QMainWindow
from QtGui import Ui_MainWindow
from PyQt6.QtCore import pyqtSignal, QObject
class communicate(QObject):
    messenge = pyqtSignal()
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.c = communicate()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.button.clicked.connect(self.count_down)
        self.c.messenge.connect(self.close_message)
    def count_down(self):
        self.uic.listWidget.addItem("hello")
        if self.uic.listWidget.count() % 4 == 0:
            self.c.messenge.emit()
    def close_message(self):
        self.uic.listWidget.close()
        self.uic.label.setText("da tat")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())