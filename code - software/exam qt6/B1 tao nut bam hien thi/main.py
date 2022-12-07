import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from QtGui import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
    # Khai bao nut click
        self.uic.button_batdau.clicked.connect(self.showScreen)
    # thay doi chu o screen
        self.uic.button_ketthuc.clicked.connect(self.main_win.close)
    def showScreen(self):
    # Doi text tren man hinh
        self.uic.screen.setText('da mo')


    def show(self):
        # command to run
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
