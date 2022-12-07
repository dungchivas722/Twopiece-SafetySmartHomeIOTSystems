import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from QtGui import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
# Khai bao code
    #khai bao nut hien page 1
        self.uic.button_screen1.clicked.connect(self.showScreen1)
        self.uic.button_screen2.clicked.connect(self.showScreen2)
        self.uic.button_screen3.clicked.connect(self.showScreen3)
    #hien screen 1
    def showScreen1(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.page_1)
    #hien screen 2
    def showScreen2(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.page_2)
    #hien screen 3
    def showScreen3(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.page_3)
    def show(self):
        # command to run
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
