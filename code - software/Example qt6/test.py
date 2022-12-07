import sys
# pip install pyqt5
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow
from QtGuiTest import Ui_MainWindow
import time
import serial
import requests
token="ct4pGWM0b_PkftQNA1lv0pFcYOlN0Max"
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.timer4 = QtCore.QTimer()
        self.timer4.setInterval(50)
        self.timer4.timeout.connect(self.blynk)
        self.timer4.start(100)
    def blynk(self):
        self.battatmodulekhi = self.read( "v0")
        self.khigas = self.read("v1")
        self.battatmodulenhietdo = self.read("v2")
        self.nhietdo = self.read("v3")
        self.battatmoduleamthanh = self.read("v4")
        self.battatmodulerung = self.read("v5")
        self.battatmodulesuckhoe = self.read("v6")
        self.suckhoenguoithuong = self.read("v7")
        self.modulechuyendong  = self.read("v8")
        self.themvantay = self.read("v9")
        self.loichuyendong = self.read("v10")


    def write(self,pin,value):
        api_url = "https://blynk.cloud/external/api/update?token="+token+"&"+pin+"="+value
        response = requests.get(api_url)
        if "200" in str(response):
            print("Value successfully updated")
        else:
            print("Could not find the device token or wrong pin format")

    def read(self,pin):
        api_url = "https://blynk.cloud/external/api/get?token="+token+"&"+pin
        response = requests.get(api_url)
        return response.content.decode()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    #main_win.show()
    sys.exit(app.exec())