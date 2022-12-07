#!/usr/bin/python

from PyQt5 import QtCore, QtGui, QtNetwork
import sys


class Example:

    def __init__(self):
        self.timer4 = QtCore.QTimer()
        self.timer4.setInterval(50)
        self.timer4.timeout.connect(self.blynk)
        self.timer4.start(1000)
    def blynk(self):
        self.doRequest("v0")
        self.doRequest1("v1")
    def doRequest(self,pin):

        url = "https://blynk.cloud/external/api/get?token=ct4pGWM0b_PkftQNA1lv0pFcYOlN0Max&" + pin
        req = QtNetwork.QNetworkRequest(QtCore.QUrl(url))
        self.nam = QtNetwork.QNetworkAccessManager()
        self.nam.get(req)
        self.nam.finished.connect(self.handleResponse)

    def handleResponse(self, reply):
        bytes_string = reply.readAll()
        print("gia tri thu 1 :"+str(bytes_string, 'utf-8'))
    def doRequest1(self,pin):

        url = "https://blynk.cloud/external/api/get?token=ct4pGWM0b_PkftQNA1lv0pFcYOlN0Max&" + pin
        req = QtNetwork.QNetworkRequest(QtCore.QUrl(url))
        self.nam1 = QtNetwork.QNetworkAccessManager()
        self.nam1.get(req)
        self.nam1.finished.connect(self.handleResponse1)

    def handleResponse1(self, reply):
        bytes_string = reply.readAll()
        print("gia tri thu 2 :"+str(bytes_string, 'utf-8'))




if __name__ == '__main__':
    app = QtCore.QCoreApplication([])
    ex = Example()
    sys.exit(app.exec())