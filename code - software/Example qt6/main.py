import sys
# pip install pyqt6
from turtle import delay

from PyQt5.QtGui import QMovie
from PyQt5.QtMultimedia import QSoundEffect, QMediaPlayer, QAudioOutput
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QLineEdit, QTextEdit, QGridLayout, QPushButton, \
    QHBoxLayout
from PyQt5.QtCore import pyqtSignal, QTimer, QTime, QDate, QCoreApplication, QUrl
from PyQt5 import QtCore, QtNetwork, QtWidgets, Qt
from QtGui import Ui_MainWindow
from random import randint
import pyqtgraph as pg
import time
import array as arr
import requests
from datetime import timedelta
token="ct4pGWM0b_PkftQNA1lv0pFcYOlN0Max"
class MainWindow(QMainWindow):
    def test(self):
        line = "7029115810"
        if len(line) == 10:
            doam = line[0] + line[1]
            nhietdo = line[2] + line[3]
            den = int(line[4])
            gas = int(line[5])
            phantramgas = line[6] + line[7]
            amthanh = int(line[8])
            rung = int(line[9])
            if gas==1:
                self.uic.giatrikhi.setText("trong lành")
            elif gas==0:
                self.uic.giatrikhi.setText("khí độc")
            else:
                self.uic.giatrikhi.setText("nguy hiểm")
            if den==1:
                self.uic.giatritroisang.show()
                self.uic.giatritroitoi.hide()
            else:
                self.uic.giatritroisang.show()
                self.uic.giatritroitoi.hide()
            if amthanh==1:
                self.uic.giatriamthanhbat.show()
                self.uic.giatriamthanhtat.hide()
            else:
                self.uic.giatriamthanhtat.show()
                self.uic.giatriamthanhbat.hide()
            if rung==1:
                self.uic.giatrirungbat.show()
                self.uic.giatrirungtat.hide()
            else:
                self.uic.giatrirungbat.hide()
                self.uic.giatrirungtat.show()
            self.uic.giatridoam.setText(doam+"%")
            self.uic.giatrinhietdo.setText(nhietdo+"°C")
            self.uic.giatrigas.setText(phantramgas+"%")
            self.uic.giatrimodulesuckhoebat.show()
            self.uic.giatrimodulesuckhoetat.hide()
            self.uic.giatrimodulexamnhapbat.show()
            self.uic.giatrimodulexamnhaptat.hide()




    def update_plot_data(self):
        self.suckhoe +=1
        timeday = QTime.currentTime()
        timefull = timeday.toString('hh:mm:ss') + " " + QDate.currentDate().toString()
        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.

        self.y = self.y[1:]  # Remove the first
        if self.giatrisuckhoe == 1:
            self.y.append(randint(70,80))  # Add a new random value.
        else:
            self.y.append(0)
        self.uic.thoigiansuckhoeModule.setText(timefull)
        self.uic.nhiptimsuckhoeModule.setText(str(self.y[-1]))
        self.data_line.setData(self.x, self.y)  # Update the data.

    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # self.movie = QMovie("logonhom.gif")
        # self.uic.labelLogo.setMovie(self.movie)
        # self.movie.start()
        #self.test()
        self.giatrisuckhoe = 0
        CITY = "Hanoi"
        API_KEY = "e7269686f82e99e28176c2b3b658c510"
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
        self.response = requests.get(url).json()



        self.graphWidget = pg.PlotWidget()
        self.uic.grahp.addWidget(self.graphWidget)
        #self.x = list(range(5))  # 100 time points
        self.x = [0] * 5
        self.y = [0] * 5 # 100 data points

        self.graphWidget.setBackground('w')

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.graphWidget.plot(self.x, self.y, pen=pen)

        self.timer2 = QtCore.QTimer()
        self.timer2.setInterval(50)
        self.timer2.timeout.connect(self.update_plot_data)
        self.timer2.start(1000)
        self.suckhoe =0

        timer = QTimer(self)
        timer.timeout.connect(self.loop)
        timer.start(1000)
        self.loadNhatKyVanTay()
        self.loadNhatKyPhatHien()
        self.loadNhatKySucKhoe()
        self.loadCaiDatVanTay()
        # Khai bao code
        # ------------------------------------------------------------------------
        # Khai bao cam bien
            #Khai bao van tay

        #---------------------------------------------------------------------------
        # khai bao menu
        # khai bao nut hien main

        # hien screen 1
        self.sound =1
        self.uic.settingButton.clicked.connect(self.showMainSetting)
        self.uic.advanceButton.clicked.connect(self.showMainAdvance)
        self.uic.backButton.clicked.connect(self.showMainCore)
        self.uic.backButton1.clicked.connect(self.showMainCore)
        self.uic.backButton2.clicked.connect(self.showMainCore)
        self.uic.backButtonVanTay.clicked.connect(self.showMainSetting)
        self.uic.falseSoundButton.clicked.connect(self.showFalseSoundButton)
        self.uic.trueSoundButton.clicked.connect(self.showTrueSoundButton)
        self.uic.vantayButton.clicked.connect(self.showMainVanTay)
        self.uic.suckhoeButton.clicked.connect(self.showMainAdvance)
        self.uic.phathienButton.clicked.connect(self.showMainPhatHien)
        self.uic.settingvantayButton.clicked.connect(self.showMainSettingVanTay)
        # ban phim
        self.uic.qButton.clicked.connect(self.qShowKey)
        self.uic.wButton.clicked.connect(self.wShowKey)
        self.uic.eButton.clicked.connect(self.eShowKey)
        self.uic.rButton.clicked.connect(self.rShowKey)
        self.uic.tButton.clicked.connect(self.tShowKey)
        self.uic.yButton.clicked.connect(self.yShowKey)
        self.uic.uButton.clicked.connect(self.uShowKey)
        self.uic.iButton.clicked.connect(self.iShowKey)
        self.uic.oButton.clicked.connect(self.oShowKey)
        self.uic.pButton.clicked.connect(self.pShowKey)
        self.uic.aButton.clicked.connect(self.aShowKey)
        self.uic.sButton.clicked.connect(self.sShowKey)
        self.uic.dButton.clicked.connect(self.dShowKey)
        self.uic.fButton.clicked.connect(self.fShowKey)
        self.uic.gButton.clicked.connect(self.gShowKey)
        self.uic.hButton.clicked.connect(self.hShowKey)
        self.uic.jButton.clicked.connect(self.jShowKey)
        self.uic.kButton.clicked.connect(self.kShowKey)
        self.uic.lButton.clicked.connect(self.lShowKey)
        self.uic.zButton.clicked.connect(self.zShowKey)
        self.uic.xButton.clicked.connect(self.xShowKey)
        self.uic.cButton.clicked.connect(self.cShowKey)
        self.uic.vButton.clicked.connect(self.vShowKey)
        self.uic.bButton.clicked.connect(self.bShowKey)
        self.uic.nButton.clicked.connect(self.nShowKey)
        self.uic.mButton.clicked.connect(self.mShowKey)
        self.uic.motButton.clicked.connect(self.motButtonShow)
        self.uic.haiButton.clicked.connect(self.haiButtonShow)
        self.uic.baButton.clicked.connect(self.baButtonShow)
        self.uic.bonButton.clicked.connect(self.bonButtonShow)
        self.uic.namButton.clicked.connect(self.namButtonShow)
        self.uic.sauButton.clicked.connect(self.sauButtonShow)
        self.uic.bayButton.clicked.connect(self.bayButtonShow)
        self.uic.tamButton.clicked.connect(self.tamButtonShow)
        self.uic.chinButton.clicked.connect(self.chinButtonShow)
        self.uic.backNumberButton.clicked.connect(self.backButtonNumberShow)
        self.uic.clearNumberButton.clicked.connect(self.clearButtonNumberShow)
        self.uic.deleteButton.clicked.connect(self.deleteShowKey)
        self.uic.backkeyboardButton.clicked.connect(self.backkeyboardButtonShow)
        # nut nhat ky van tay
        self.effect1 = QSoundEffect(QCoreApplication.instance())
        self.effect2 = QSoundEffect(QCoreApplication.instance())
        self.uic.xoatatcanhatkyvantayButton.clicked.connect(self.showxoatatcanhatkyvantay)
        self.uic.xoamotcainhatkyvantayButton.clicked.connect(self.showxoamotcainhatkyvantay)
        self.uic.xoatatcanhatkyphathienButton.clicked.connect(self.showxoatatcanhatkyphathien)
        self.uic.xoamotcainhatkyphathienButton.clicked.connect(self.showxoamotcainhatkyphathien)
        self.uic.xoatatcanhatkysuckhoeButton.clicked.connect(self.showxoatatcanhatkysuckhoe)
        self.uic.xoamotcainhatkysuckhoeButton.clicked.connect(self.showxoamotcainhatkysuckhoe)
        # nut nhan cac module
        #self.uic.suckhoeModuleButton.clicked.connect(self.showsuckhoeModule) show module suc khoe
        self.uic.backsuckhoeModule.clicked.connect(self.showbackModule)
        self.uic.themvantayButton.clicked.connect(self.showthemvantay)
        self.uic.enterButtonKeyBoard.clicked.connect(self.showenterButtonKeyBoard)
        self.uic.backButtonNumber.clicked.connect(self.showbackButtonNumber) #quay lai ban phim
        self.uic.enterButtonNumber.clicked.connect(self.showenterButtonNumber)
        self.uic.backxacnhanButton.clicked.connect(self.showbackxacnhanButton)
        self.uic.xacnhanButton.clicked.connect(self.showxacnhanButton)
        self.uic.Ok1.hide()
        self.uic.Ok2.hide()
        self.uic.OK3.hide()
        self.uic.Ok4.hide()
        self.uic.thanhcong.hide()
        self.uic.progressBar.setValue(0)
        self.uic.huybo.clicked.connect(self.showMainCore)
        self.a = 0
        self.b = 0
        self.list = [0]*5
        for x in range(5):
            self.list[x]=x
            print(self.list[x])
        self.vitri = 1
        self.uic.premusicButton.clicked.connect(self.showpremusic)
        self.uic.aftermusicButton.clicked.connect(self.showaftermusic)
        self.uic.pausemusicButton.clicked.connect(self.showpausemusic)
        self.uic.playmusicButton.clicked.connect(self.showplaymusic)
        self.play_sound(self.vitri,1) #bat nhac
        self.uic.playmusicButton.hide()
        self.uic.pausemusicButton.show()
        self.uic.trueSoundButton.clicked.connect(self.showtatamthanh)
        self.uic.falseSoundButton.clicked.connect(self.showbatamthanh)
        self.timer4 = QtCore.QTimer()
        self.timer4.timeout.connect(self.blynk)
        self.timer4.start(300)
        self.dkmodulekhi=0
        self.dkkhigas=0
        self.dkmodulenhietdo=0
        self.dknhietdo = 0
        self.dkmoduleamthanh = "0"
        self.dkmodulerung = "0"
        self.dkmodulesuckhoe = "0"
        self.dksuckhoenguoithuong = "0"
        self.dkmodulechuyendong = "0"
        self.dkthemvantay = "0"
        self.dkloichuyendong = "0"
        self.dkloithoatmain = "0"
        self.dkanhsang = "0"
        self.dkngoaivi = "0"
        self.dkloimodule = "0"
        self.dkloihethong = "0"
        self.uic.Module.setCurrentWidget(self.uic.moduleKhiOn)
        self.uic.radiokhithapButton.setChecked(True)
        self.uic.radiongoaivithapButton.setChecked(True)
        self.uic.radionhietdoButton.setChecked(True)
        self.uic.checkBox.setChecked(True)
        self.uic.checkBox2.setChecked(True)
        self.uic.checkBox3.setChecked(True)
        self.uic.checkBox4.setChecked(True)
        self.uic.checkBox5.setChecked(True)
        self.uic.resetButton.clicked.connect(self.showreset)
        self.uic.xoavantayButton.clicked.connect(self.showxoamotcaicaidatvantay)
        self.uic.loichuyendong.hide()
        self.doc = 0
        self.doc2 =0
    def showreset(self):
        self.uic.radiokhithapButton.setChecked(True)
        self.uic.radiongoaivithapButton.setChecked(True)
        self.uic.radionhietdoButton.setChecked(True)
        self.uic.checkBox.setChecked(True)
        self.uic.checkBox2.setChecked(True)
        self.uic.checkBox3.setChecked(True)
        self.uic.checkBox4.setChecked(True)
        self.uic.checkBox5.setChecked(True)
    def blynk(self):
        self.doRequest("v0")
        self.doRequest1("v1")
        self.doRequest2("v2")
        self.doRequest3("v3")
        self.doRequest4("v4")
        self.doRequest5("v5")
        self.doRequest6("v6")
        self.doRequest7("v7")
        self.doRequest8("v8")
        self.doRequest9("v9")
        self.doRequest10("v10")
        self.doRequest11("v11")
        self.doRequest12("v12")
        self.doRequest13("v13")
        self.doRequest14("v14")
        self.doRequest15("v15")
        if self.dkmodulekhi == '0':
            self.uic.onModuleKhi.hide()
            self.uic.offModuleKhi.show()
            self.uic.giatrikhi.setText("đang tải...")
            self.uic.giatrigas.setText("đang tải...")
        else:
            self.uic.onModuleKhi.show()
            self.uic.offModuleKhi.hide()
            if int(self.dkkhigas) <= 40:
                self.doc1 = 0
                self.effect2.stop()
                self.uic.giatrikhi.setText("trong lành")
                self.uic.giatrigas.setText(str(self.dkkhigas))
                print(self.doc1)
            elif int(self.dkkhigas) > 40 and int(self.dkkhigas) < 70:
                self.doc1 += 1
                self.uic.giatrikhi.setText("khí độc")
                self.uic.giatrigas.setText(str(self.dkkhigas))
                if self.doc1 == 1 :
                    self.play_canhbao2("ga",self.sound)
                    print(self.doc1)
            else:
                self.doc1 += 1
                self.uic.giatrikhi.setText("nguy hiểm")
                self.uic.giatrigas.setText(str(self.dkkhigas))
                if self.doc1 == 1 :
                    self.play_canhbao2("ga",self.sound)
                    print(self.doc1)
        if self.dkmodulenhietdo == '0':
            self.uic.onModuleNhietDo.hide()
            self.uic.offModuleNhietDo.show()
            self.uic.giatrinhietdo.setText("đang tải...")
            self.uic.giatridoam.setText("đang tải...")
        else:
            self.uic.onModuleNhietDo.show()
            self.uic.offModuleNhietDo.hide()
            self.uic.giatrinhietdo.setText(str(self.dknhietdo))
            giatridoam1 = str(self.response['main']['humidity'])
            self.uic.giatridoam.setText(giatridoam1)
        if self.dkanhsang == '0':
            self.uic.giatritroitoi.show()
            self.uic.giatritroisang.hide()
        else:
            self.uic.giatritroitoi.hide()
            self.uic.giatritroisang.show()
        if self.dkmoduleamthanh == '0':
            self.uic.giatriamthanhtat.show()
            self.uic.giatriamthanhbat.hide()
        else:
            self.uic.giatriamthanhbat.show()
            self.uic.giatriamthanhtat.hide()
        if self.dkmodulerung == '0':
            self.uic.giatrirungtat.show()
            self.uic.giatrirungbat.hide()
        else:
            self.uic.giatrirungbat.show()
            self.uic.giatrirungtat.hide()
        if self.dkmodulesuckhoe == '0':
            self.uic.giatrimodulesuckhoetat.show()
            self.uic.giatrimodulesuckhoebat.hide()
        else:
            self.uic.giatrimodulesuckhoebat.show()
            self.uic.giatrimodulesuckhoetat.hide()
        if self.dkmodulesuckhoe == '0':
            self.uic.giatrimodulesuckhoetat.show()
            self.uic.giatrimodulesuckhoebat.hide()
        else:
            self.uic.giatrimodulesuckhoebat.show()
            self.uic.giatrimodulesuckhoetat.hide()
        if self.dkmodulechuyendong == '0':
            self.uic.giatrimodulexamnhaptat.show()
            self.uic.giatrimodulexamnhapbat.hide()
            self.uic.loichuyendong.hide()
        else:
            self.uic.giatrimodulexamnhaptat.hide()
            self.uic.giatrimodulexamnhapbat.show()
            if self.dkloichuyendong == "1":
                self.doc+= 1
                self.uic.loichuyendong.show()
                if self.doc == 1:
                    self.play_canhbao("xamnhap",self.sound)
                    self.themNhatKyPhatHien(" nguoi dung ")
            else:
                self.doc = 0
                self.uic.loichuyendong.hide()
                self.effect1.stop()
        if self.dkmodulesuckhoe == '1' or self.dkmodulechuyendong == '1':
            self.uic.offModuleKhac.hide()
            self.uic.onModuleKhac.show()
        else:
            self.uic.onModuleKhac.hide()
            self.uic.offModuleKhac.show()
        if self.dksuckhoenguoithuong == '1':
            self.showsuckhoenguoithuong()
            self.giatrisuckhoe = 1
        else:
            self.giatrisuckhoe = 0
            self.themNhatKySucKhoe()
        if self.dkngoaivi == "1":
            self.uic.offModuleNgoaiVi.hide()
            self.uic.onModuleNgoaiVi.show()
        else:
            self.uic.onModuleNgoaiVi.hide()
            self.uic.offModuleNgoaiVi.show()

        if self.dkloithoatmain == "1":
            self.showMainCore()
        if self.dkloihethong == "0":
            self.uic.trueWifiButton_6.hide()
        else:
            self.uic.trueWifiButton_6.show()
        if self.dkloimodule == "0":
            self.uic.trueWifiButton_7.hide()
        else:
            self.uic.trueWifiButton_7.show()
    def showsuckhoenguoithuong(self):
        self.showsuckhoeModule()

    def doRequest(self, pin):
        url = "https://blynk.cloud/external/api/get?token=ct4pGWM0b_PkftQNA1lv0pFcYOlN0Max&" + pin
        req = QtNetwork.QNetworkRequest(QtCore.QUrl(url))
        self.nam = QtNetwork.QNetworkAccessManager()
        self.nam.get(req)
        self.nam.finished.connect(self.handleResponse)
    def handleResponse(self, reply):
        bytes_string = reply.readAll()
        self.dkmodulekhi = str(bytes_string, 'utf-8')
    def doRequest1(self, pin):
        url = "https://blynk.cloud/external/api/get?token=ct4pGWM0b_PkftQNA1lv0pFcYOlN0Max&" + pin
        req = QtNetwork.QNetworkRequest(QtCore.QUrl(url))
        self.nam1 = QtNetwork.QNetworkAccessManager()
        self.nam1.get(req)
        self.nam1.finished.connect(self.handleResponse1)
    def handleResponse1(self, reply):
        bytes_string = reply.readAll()
        self.dkkhigas = str(bytes_string, 'utf-8')
    def doRequest2(self, pin):
        url = "https://blynk.cloud/external/api/get?token=ct4pGWM0b_PkftQNA1lv0pFcYOlN0Max&" + pin
        req = QtNetwork.QNetworkRequest(QtCore.QUrl(url))
        self.nam2 = QtNetwork.QNetworkAccessManager()
        self.nam2.get(req)
        self.nam2.finished.connect(self.handleResponse2)
    def handleResponse2(self, reply):
        bytes_string = reply.readAll()
        self.dkmodulenhietdo = str(bytes_string, 'utf-8')
    def doRequest3(self, pin):
        url = "https://blynk.cloud/external/api/get?token=ct4pGWM0b_PkftQNA1lv0pFcYOlN0Max&" + pin
        req = QtNetwork.QNetworkRequest(QtCore.QUrl(url))
        self.nam3 = QtNetwork.QNetworkAccessManager()
        self.nam3.get(req)
        self.nam3.finished.connect(self.handleResponse3)
    def handleResponse3(self, reply):
        bytes_string = reply.readAll()
        self.dknhietdo = str(bytes_string, 'utf-8')
    def doRequest4(self, pin):
        url = "https://blynk.cloud/external/api/get?token=ct4pGWM0b_PkftQNA1lv0pFcYOlN0Max&" + pin
        req = QtNetwork.QNetworkRequest(QtCore.QUrl(url))
        self.nam4 = QtNetwork.QNetworkAccessManager()
        self.nam4.get(req)
        self.nam4.finished.connect(self.handleResponse4)
    def handleResponse4(self, reply):
        bytes_string = reply.readAll()
        self.dkmoduleamthanh = str(bytes_string, 'utf-8')
    def doRequest5(self, pin):
        url = "https://blynk.cloud/external/api/get?token=ct4pGWM0b_PkftQNA1lv0pFcYOlN0Max&" + pin
        req = QtNetwork.QNetworkRequest(QtCore.QUrl(url))
        self.nam5 = QtNetwork.QNetworkAccessManager()
        self.nam5.get(req)
        self.nam5.finished.connect(self.handleResponse5)
    def handleResponse5(self, reply):
        bytes_string = reply.readAll()
        self.dkmodulerung = str(bytes_string, 'utf-8')
    def doRequest6(self, pin):
        url = "https://blynk.cloud/external/api/get?token=ct4pGWM0b_PkftQNA1lv0pFcYOlN0Max&" + pin
        req = QtNetwork.QNetworkRequest(QtCore.QUrl(url))
        self.nam6 = QtNetwork.QNetworkAccessManager()
        self.nam6.get(req)
        self.nam6.finished.connect(self.handleResponse6)
    def handleResponse6(self, reply):
        bytes_string = reply.readAll()
        self.dkmodulesuckhoe = str(bytes_string, 'utf-8')
    def doRequest7(self, pin):
        url = "https://blynk.cloud/external/api/get?token=ct4pGWM0b_PkftQNA1lv0pFcYOlN0Max&" + pin
        req = QtNetwork.QNetworkRequest(QtCore.QUrl(url))
        self.nam7 = QtNetwork.QNetworkAccessManager()
        self.nam7.get(req)
        self.nam7.finished.connect(self.handleResponse7)
    def handleResponse7(self, reply):
        bytes_string = reply.readAll()
        self.dksuckhoenguoithuong = str(bytes_string, 'utf-8')
    def doRequest8(self, pin):
        url = "https://blynk.cloud/external/api/get?token=ct4pGWM0b_PkftQNA1lv0pFcYOlN0Max&" + pin
        req = QtNetwork.QNetworkRequest(QtCore.QUrl(url))
        self.nam8 = QtNetwork.QNetworkAccessManager()
        self.nam8.get(req)
        self.nam8.finished.connect(self.handleResponse8)
    def handleResponse8(self, reply):
        bytes_string = reply.readAll()
        self.dkmodulechuyendong = str(bytes_string, 'utf-8')

    def doRequest9(self, pin):
        url = "https://blynk.cloud/external/api/get?token=ct4pGWM0b_PkftQNA1lv0pFcYOlN0Max&" + pin
        req = QtNetwork.QNetworkRequest(QtCore.QUrl(url))
        self.nam9 = QtNetwork.QNetworkAccessManager()
        self.nam9.get(req)
        self.nam9.finished.connect(self.handleResponse9)

    def handleResponse9(self, reply):
        bytes_string = reply.readAll()
        self.dkthemvantay = str(bytes_string, 'utf-8')
    def doRequest10(self, pin):
        url = "https://blynk.cloud/external/api/get?token=ct4pGWM0b_PkftQNA1lv0pFcYOlN0Max&" + pin
        req = QtNetwork.QNetworkRequest(QtCore.QUrl(url))
        self.nam10 = QtNetwork.QNetworkAccessManager()
        self.nam10.get(req)
        self.nam10.finished.connect(self.handleResponse10)

    def handleResponse10(self, reply):
        bytes_string = reply.readAll()
        self.dkloichuyendong = str(bytes_string, 'utf-8')
    def doRequest11(self, pin):
        url = "https://blynk.cloud/external/api/get?token=ct4pGWM0b_PkftQNA1lv0pFcYOlN0Max&" + pin
        req = QtNetwork.QNetworkRequest(QtCore.QUrl(url))
        self.nam11 = QtNetwork.QNetworkAccessManager()
        self.nam11.get(req)
        self.nam11.finished.connect(self.handleResponse11)

    def handleResponse11(self, reply):
        bytes_string = reply.readAll()
        self.dkloithoatmain = str(bytes_string, 'utf-8')
    def doRequest12(self, pin):
        url = "https://blynk.cloud/external/api/get?token=ct4pGWM0b_PkftQNA1lv0pFcYOlN0Max&" + pin
        req = QtNetwork.QNetworkRequest(QtCore.QUrl(url))
        self.nam12 = QtNetwork.QNetworkAccessManager()
        self.nam12.get(req)
        self.nam12.finished.connect(self.handleResponse12)
    def handleResponse12(self, reply):
        bytes_string = reply.readAll()
        self.dkanhsang = str(bytes_string, 'utf-8')
    def doRequest13(self, pin):
        url = "https://blynk.cloud/external/api/get?token=ct4pGWM0b_PkftQNA1lv0pFcYOlN0Max&" + pin
        req = QtNetwork.QNetworkRequest(QtCore.QUrl(url))
        self.nam13 = QtNetwork.QNetworkAccessManager()
        self.nam13.get(req)
        self.nam13.finished.connect(self.handleResponse13)
    def handleResponse13(self, reply):
        bytes_string = reply.readAll()
        self.dkngoaivi = str(bytes_string, 'utf-8')
    def doRequest14(self, pin):
        url = "https://blynk.cloud/external/api/get?token=ct4pGWM0b_PkftQNA1lv0pFcYOlN0Max&" + pin
        req = QtNetwork.QNetworkRequest(QtCore.QUrl(url))
        self.nam14 = QtNetwork.QNetworkAccessManager()
        self.nam14.get(req)
        self.nam14.finished.connect(self.handleResponse14)
    def handleResponse14(self, reply):
        bytes_string = reply.readAll()
        self.dkloihethong = str(bytes_string, 'utf-8')

    def doRequest15(self, pin):
        url = "https://blynk.cloud/external/api/get?token=ct4pGWM0b_PkftQNA1lv0pFcYOlN0Max&" + pin
        req = QtNetwork.QNetworkRequest(QtCore.QUrl(url))
        self.nam15 = QtNetwork.QNetworkAccessManager()
        self.nam15.get(req)
        self.nam15.finished.connect(self.handleResponse15)

    def handleResponse15(self, reply):
        bytes_string = reply.readAll()
        self.dkloimodule = str(bytes_string, 'utf-8')
    def showbatamthanh(self):
        self.sound=1
        self.effect.setVolume(self.sound)
        self.uic.Sound.setCurrentWidget(self.uic.trueSound)
    def showtatamthanh(self):
        self.sound=0
        self.effect.setVolume(self.sound)
        self.uic.Sound.setCurrentWidget(self.uic.falseSound)
    def showplaymusic(self):
        self.effect.stop()
        self.play_sound(self.vitri, 1)  # bat nhac
        self.uic.playmusicButton.hide()
        self.uic.pausemusicButton.show()
    def showpausemusic(self):
        self.effect.stop()
        self.uic.playmusicButton.show()
        self.uic.pausemusicButton.hide()
    def showpremusic(self):
        self.effect.stop() # bat nhac
        if self.list[self.vitri] == 0:
            self.vitri = len(self.list)-1
        else:
            self.vitri -= 1
        self.play_sound(self.vitri, 1)  # bat nhac
        self.uic.playmusicButton.hide()
        self.uic.pausemusicButton.show()
    def showaftermusic(self):
        self.effect.stop() # bat nhac
        if self.list[self.vitri] == (len(self.list)-1):
            self.vitri = 0
        else:
            self.vitri += 1
        self.play_sound(self.vitri, 1)  # bat nhac
        self.uic.playmusicButton.hide()
        self.uic.pausemusicButton.show()
    def program(self,a,b):
            while a<b :
                time.sleep(0.01)
                a += 1
                self.uic.progressBar.setValue(a)
    def xacnhanvantay(self):
        self.b=0
        self.d=0
        print("b la: ",self.b)
        self.uic.huybo.hide()
        self.uic.Module.setCurrentWidget(self.uic.Modulenhanvantay)
        self.timer1 = QTimer(self)
        self.timer1.timeout.connect(self.dem)

        self.timer1.start(200)

        self.uic.progressBar2.setValue(0)
        self.timer0 = QTimer(self)
        self.timer0.timeout.connect(self.dem1)
        self.timer0.start(200)


    def dem1(self):
        if self.dkthemvantay == "1":
            print(self.dkthemvantay)
            self.d+= 1
            if self.d == 10:
                self.uic.nhanantaynguoidung.setText("an tay thanh cong")
                self.uic.thanhcong.setText("Thành công")
                self.uic.thanhcong.show()
            if self.d == 20:
                self.uic.thanhcong.hide()
                self.uic.thanhcong.setText("Thành công")
                self.saveCaiDatVanTay()
                self.showMainCore()
                self.timer1.stop()
                self.timer0.stop()
                item = " nguoi dung : " + self.uic.xacNhanKeyboard.text() + "co id :" + self.uic.xacNhanNumber.text() + " " + "thoi gian : " + self.uic.xacNhanThoiGian.text() + '\n'
                self.uic.listquanlyVanTay.addItem(item)
                self.uic.nhanantaynguoidung.setText("Nhấn tay vào module 2 lần")

    def saveCaiDatVanTay(self):
        with open('caidatvantay.txt', 'w') as f:
            list_widget = self.uic.listquanlyVanTay
            entries = '\n'.join(list_widget.item(ii).text() for ii in range(list_widget.count()))
            f.write(entries)
    def dem(self):
        self.b += 1
        self.uic.progressBar2.setValue(self.b)
        if self.b == 100:
            self.uic.thanhcong.setText("Hủy bỏ")
            self.uic.thanhcong.show()
        if self.b == 110:
            self.uic.thanhcong.hide()
            self.uic.thanhcong.setText("Thành công")
            self.showMainCore()
            self.timer1.stop()

    def showxacnhanButton(self):
        nhaptextten = self.uic.xacNhanKeyboard.text()
        nhaptextid = self.uic.xacNhanNumber.text()
        nhapthoigian = self.uic.xacNhanThoiGian.text()
        if nhaptextid == "" and nhaptextten == "":
            self.uic.xacnhanthongtin.setText("Cần nhập tên và số id")
        elif nhaptextid == "" and nhaptextten != "":
            self.uic.xacnhanthongtin.setText("Cần nhập số id")
        elif nhaptextid != "" and nhaptextten == "":
            self.uic.xacnhanthongtin.setText("Cần nhập tên")
        else:
            self.program(40, 60)
            self.uic.OK3.show()
            self.xacnhanvantay()
            # nhaplist ="nguoi dung: "+ nhaptextten + " da luu van tay voi ma id: " + nhaptextid + " vao thoi gian: "+ nhapthoigian +'\n'
            # self.uic.xacnhanthongtin.setText("Xác nhận thông tin")
            # self.uic.listquanlyVanTay.addItem(nhaplist)

    def showbackxacnhanButton(self):
        self.uic.Module.setCurrentWidget(self.uic.ModuleNumber)
        self.program(0,20)
        self.uic.OK3.hide()
        self.uic.Ok2.hide()
        self.uic.Ok1.hide()
        self.uic.nhapText.setText("")
        self.uic.nhapTextNumber.setText("")
    def showenterButtonNumber(self):
        self.program(20,40)
        self.uic.Ok2.show()
        self.uic.Module.setCurrentWidget(self.uic.ModuleXacNhan)
        nhaptextten = self.uic.nhapText.text()
        self.uic.xacNhanKeyboard.setText(nhaptextten)
        nhaptextid = self.uic.nhapTextNumber.text()
        self.uic.xacNhanNumber.setText(nhaptextid)
        self.uic.xacNhanThoiGian.setText(" "+QTime.currentTime().toString() + " " + QDate.currentDate().toString())

    def showbackButtonNumber(self):
        self.uic.Module.setCurrentWidget(self.uic.ModuleKeyboard)
        self.uic.progressBar.setValue(0)
        self.uic.Ok1.hide()
        self.uic.Ok2.hide()
        self.uic.OK3.hide()
        self.uic.nhapTextNumber.setText("")
    def showenterButtonKeyBoard(self):
        self.program(0, 20)
        self.uic.Ok1.show()
        self.uic.Module.setCurrentWidget(self.uic.ModuleNumber)
    def showthemvantay(self):
        self.uic.Module.setCurrentWidget(self.uic.ModuleKeyboard)
        self.uic.Menu.setCurrentWidget(self.uic.Menuthemvantay)
    def showbackModule(self):
        self.uic.Module.setCurrentWidget(self.uic.ModuleCore)
    def showsuckhoeModule(self):
        self.uic.Module.setCurrentWidget(self.uic.ModuleSucKhoe)
    def showxoamotcainhatkysuckhoe(self):
        currentset = self.uic.listNhatKySucKhoe.currentRow()
        self.uic.listNhatKySucKhoe.takeItem(currentset)
        self.saveNhatKySucKhoe()
    def showxoamotcaicaidatvantay(self):
        currentset = self.uic.listquanlyVanTay.currentRow()
        self.uic.listquanlyVanTay.takeItem(currentset)
        self.saveCaiDatVanTay()
    def showxoatatcanhatkysuckhoe(self):
        self.uic.listNhatKySucKhoe.clear()
        self.saveNhatKySucKhoe()
    def themNhatKySucKhoe(self):
        item = " Do duoc " +  self.uic.nhiptimsuckhoeModule.text() + " vao thoi gian " + self.uic.thoigiansuckhoeModule.text() +'\n'
        if self.uic.nhiptimsuckhoeModule.text() != "0" and self.uic.nhiptimsuckhoeModule.text() != "" :
            self.uic.listNhatKySucKhoe.addItem(item)
        self.saveNhatKySucKhoe()
    def loadNhatKySucKhoe(self):
        with open('nhatkysuckhoe.txt', 'r') as test:
            for movie in test:
                if movie.strip() == '': continue
                self.uic.listNhatKySucKhoe.addItem(movie)
    def loadCaiDatVanTay(self):
        with open('caidatvantay.txt', 'r') as test:
            for movie in test:
                if movie.strip() == '': continue
                self.uic.listquanlyVanTay.addItem(movie)
    def saveNhatKySucKhoe(self):
        with open('nhatkysuckhoe.txt', 'w') as f:
            list_widget = self.uic.listNhatKySucKhoe
            entries = '\n'.join(list_widget.item(ii).text() for ii in range(list_widget.count()))
            f.write(entries)
    def showxoamotcainhatkyvantay(self):
        currentset = self.uic.listNhatKyVanTay.currentRow()
        self.uic.listNhatKyVanTay.takeItem(currentset)
        self.saveNhatKyVanTay()
    def showxoatatcanhatkyvantay(self):
        self.uic.listNhatKyVanTay.clear()
        self.saveNhatKyVanTay()
    def themNhatKyVanTay(self,name):
        item = name + " da su dung van tay " + "luc " + QTime.currentTime().toString()+" "+QDate.currentDate().toString() +'\n'
        self.uic.listNhatKyVanTay.addItem(item)
        self.saveNhatKyVanTay()
    def loadNhatKyVanTay(self):
        with open('nhatkyvantay.txt', 'r') as test:
            for movie in test:
                if movie.strip() == '': continue
                self.uic.listNhatKyVanTay.addItem(movie)
    def saveNhatKyVanTay(self):
        with open('nhatkyvantay.txt', 'w') as f:
            list_widget = self.uic.listNhatKyVanTay
            entries = '\n'.join(list_widget.item(ii).text() for ii in range(list_widget.count()))
            f.write(entries)
    def showxoamotcainhatkyphathien(self):
        currentset = self.uic.listNhatKyPhatHien.currentRow()
        self.uic.listNhatKyPhatHien.takeItem(currentset)
        self.saveNhatKyPhatHien()
    def showxoatatcanhatkyphathien(self):
        self.uic.listNhatKyPhatHien.clear()
        self.saveNhatKyPhatHien()
    def themNhatKyPhatHien(self,name):
        item = " phat hien luc " + QTime.currentTime().toString()+" "+QDate.currentDate().toString() +'\n'
        self.uic.listNhatKyPhatHien.addItem(item)
        self.saveNhatKyPhatHien()
    def loadNhatKyPhatHien(self):
        with open('nhatkyphathien.txt', 'r') as test:
            for movie in test:
                if movie.strip() == '': continue
                self.uic.listNhatKyPhatHien.addItem(movie)
    def saveNhatKyPhatHien(self):
        with open('nhatkyphathien.txt', 'w') as f:
            list_widget = self.uic.listNhatKyPhatHien
            entries = '\n'.join(list_widget.item(ii).text() for ii in range(list_widget.count()))
            f.write(entries)
    def motButtonShow(self):
        text = self.uic.nhapTextNumber.text()
        self.uic.nhapTextNumber.setText(text + "1")
    def haiButtonShow(self):
        text = self.uic.nhapTextNumber.text()
        self.uic.nhapTextNumber.setText(text + "2")
    def baButtonShow(self):
        text = self.uic.nhapTextNumber.text()
        self.uic.nhapTextNumber.setText(text + "3")
    def bonButtonShow(self):
        text = self.uic.nhapTextNumber.text()
        self.uic.nhapTextNumber.setText(text + "4")
    def namButtonShow(self):
        text = self.uic.nhapTextNumber.text()
        self.uic.nhapTextNumber.setText(text + "5")
    def sauButtonShow(self):
        text = self.uic.nhapTextNumber.text()
        self.uic.nhapTextNumber.setText(text + "6")
    def bayButtonShow(self):
        text = self.uic.nhapTextNumber.text()
        self.uic.nhapTextNumber.setText(text + "7")
    def tamButtonShow(self):
        text = self.uic.nhapTextNumber.text()
        self.uic.nhapTextNumber.setText(text + "8")
    def chinButtonShow(self):
        text = self.uic.nhapTextNumber.text()
        self.uic.nhapTextNumber.setText(text + "9")
    def backButtonNumberShow(self):
        text = self.uic.nhapTextNumber.text()
        self.uic.nhapTextNumber.setText(text[:len(text)-1])
    def clearButtonNumberShow(self):
        text = self.uic.nhapTextNumber.text()
        text =""
        self.uic.nhapTextNumber.setText(text)
    def deleteShowKey(self):
        text=""
        self.uic.nhapText.setText(text)
    def qShowKey(self):
        text = self.uic.nhapText.text()
        self.uic.nhapText.setText(text + "q")
    def wShowKey(self):
        text = self.uic.nhapText.text()
        self.uic.nhapText.setText(text + "w")
    def eShowKey(self):
        text = self.uic.nhapText.text()
        self.uic.nhapText.setText(text + "e")
    def rShowKey(self):
        text = self.uic.nhapText.text()
        self.uic.nhapText.setText(text + "r")
    def tShowKey(self):
        text = self.uic.nhapText.text()
        self.uic.nhapText.setText(text + "t")
    def yShowKey(self):
        text = self.uic.nhapText.text()
        self.uic.nhapText.setText(text + "y")
    def uShowKey(self):
        text = self.uic.nhapText.text()
        self.uic.nhapText.setText(text + "u")
    def iShowKey(self):
        text = self.uic.nhapText.text()
        self.uic.nhapText.setText(text + "i")
    def oShowKey(self):
        text = self.uic.nhapText.text()
        self.uic.nhapText.setText(text + "o")
    def pShowKey(self):
        text = self.uic.nhapText.text()
        self.uic.nhapText.setText(text + "p")
    def aShowKey(self):
        text = self.uic.nhapText.text()
        self.uic.nhapText.setText(text + "a")
    def sShowKey(self):
        text = self.uic.nhapText.text()
        self.uic.nhapText.setText(text + "s")
    def dShowKey(self):
        text = self.uic.nhapText.text()
        self.uic.nhapText.setText(text + "d")
    def fShowKey(self):
        text = self.uic.nhapText.text()
        self.uic.nhapText.setText(text + "f")
    def gShowKey(self):
        text = self.uic.nhapText.text()
        self.uic.nhapText.setText(text + "g")
    def hShowKey(self):
        text = self.uic.nhapText.text()
        self.uic.nhapText.setText(text + "h")
    def jShowKey(self):
        text = self.uic.nhapText.text()
        self.uic.nhapText.setText(text + "j")
    def kShowKey(self):
        text = self.uic.nhapText.text()
        self.uic.nhapText.setText(text + "k")
    def lShowKey(self):
        text = self.uic.nhapText.text()
        self.uic.nhapText.setText(text + "l")
    def zShowKey(self):
        text = self.uic.nhapText.text()
        self.uic.nhapText.setText(text + "z")
    def xShowKey(self):
        text = self.uic.nhapText.text()
        self.uic.nhapText.setText(text + "x")
    def cShowKey(self):
        text = self.uic.nhapText.text()
        self.uic.nhapText.setText(text + "c")
    def vShowKey(self):
        text = self.uic.nhapText.text()
        self.uic.nhapText.setText(text + "v")
    def zShowKey(self):
        text = self.uic.nhapText.text()
        self.uic.nhapText.setText(text + "z")
    def xShowKey(self):
        text = self.uic.nhapText.text()
        self.uic.nhapText.setText(text + "x")
    def cShowKey(self):
        text = self.uic.nhapText.text()
        self.uic.nhapText.setText(text + "c")
    def vShowKey(self):
        text = self.uic.nhapText.text()
        self.uic.nhapText.setText(text + "v")
    def bShowKey(self):
        text = self.uic.nhapText.text()
        self.uic.nhapText.setText(text + "b")
    def nShowKey(self):
        text = self.uic.nhapText.text()
        self.uic.nhapText.setText(text + "n")
    def mShowKey(self):
        text = self.uic.nhapText.text()
        self.uic.nhapText.setText(text + "m")
    def backkeyboardButtonShow(self):
        text = self.uic.nhapText.text()
        self.uic.nhapText.setText(text[:len(text)-1])
    def play_sound(self,vitri,sound):
        self.uic.showmusicButton.setText(str(vitri) + ".mp3")
        filename = str(self.list[vitri])+".wav"
        self.effect = QSoundEffect(QCoreApplication.instance())
        self.effect.setSource(QUrl.fromLocalFile(filename))
        self.effect.setVolume(sound)
        self.effect.play()
    def play_canhbao(self,name,sound):
        filename = name+".wav"
        self.effect1.setSource(QUrl.fromLocalFile(filename))
        self.effect1.setVolume(sound)
        self.effect1.play()
    def play_canhbao2(self,name,sound):
        filename = name+".wav"
        self.effect2.setSource(QUrl.fromLocalFile(filename))
        self.effect2.setVolume(sound)
        self.effect2.play()
    def loop(self):
        # self.suckhoe+=1
        # print(self.suckhoe)
        # if self.suckhoe == 10:
        #     print(self.suckhoe)
        #     self.showsuckhoeModule()
        url = QtCore.QUrl("https://www.google.com/")
        req = QtNetwork.QNetworkRequest(url)
        self.net_manager = QtNetwork.QNetworkAccessManager()
        self.res = self.net_manager.get(req)
        self.res.finished.connect(self.processRes)
        self.msg = QtWidgets.QMessageBox()
        self.showTime()
        temp = self.response['main']['temp']
        temp = temp - 273.15  # chuyen do f sang do c
        humidity = self.response['main']['humidity']
        description = self.response['weather'][0]['description']
        if description == "clear sky":
            description = "trời quang đãng"
        elif description == "few clouds":
            description = "trời ít mây"
        elif description == "scattered clouds":
            description = "mây rải rác"
        elif description == "broken clouds":
            description = "mây nhiều"
        elif description == "shower rain":
            description = "mưa rào"
        elif description == "rain":
            description = "trời mưa"
        elif description == "thunderstorm":
            description = "đang dông"
        elif description == "snow":
            description = "tuyết rơi"
        else: description = "sương mù"


        self.uic.nhietdohanoi.setText(str(temp)+"℃")
        self.uic.doamhanoi.setText(str(humidity))
        self.uic.thongtinhanoi.setText(description)
    def showTime(self):
        dateTime = QDate.currentDate()
        currentTime = QTime.currentTime()
        displayTxt = currentTime.toString('hh:mm:ss')
        self.uic.labelTime.setText(displayTxt)
        self.uic.labelDate.setText(dateTime.toString())

    @QtCore.pyqtSlot()
    def processRes(self):
        if self.res.bytesAvailable():
            self.uic.Wifi.setCurrentWidget(self.uic.trueWifi)
            self.uic.Cloud.setCurrentWidget(self.uic.trueCloud)
        else:
            self.uic.Wifi.setCurrentWidget(self.uic.falseWifi)
            self.uic.Cloud.setCurrentWidget(self.uic.falseCloud)

    # bat tat am
    def showFalseSoundButton(self):
        self.uic.Sound.setCurrentWidget(self.uic.trueSound)
        self.sound = 1 #sound =1 la co am thanh
    def showTrueSoundButton(self):
        self.uic.Sound.setCurrentWidget(self.uic.falseSound)
        self.sound = 0

    # bat main phan setting
    def showMainSetting(self):
        self.uic.Main.setCurrentWidget(self.uic.mainSetting)
        self.uic.Menu.setCurrentWidget(self.uic.MenuSetting)
        self.uic.Module.setCurrentWidget(self.uic.ModuleCore)


    def showMainSettingVanTay(self):
        self.uic.Main.setCurrentWidget(self.uic.mainSettingVanTay)
        self.uic.Menu.setCurrentWidget(self.uic.Menuvantay)

    # bat main phan nhat ky
    def showMainAdvance(self):
        self.uic.Main.setCurrentWidget(self.uic.mainSucKhoe)
        self.uic.Menu.setCurrentWidget(self.uic.MenuSucKhoe)

    def showMainVanTay(self):  # nhat ki van tay
        self.uic.Main.setCurrentWidget(self.uic.mainVanTay)

    def showMainPhatHien(self):  # nhat ki phat hien
        self.uic.Main.setCurrentWidget(self.uic.mainPhatHien)

    # quay lai man hinh chinh
    def showMainCore(self):
        self.uic.Main.setCurrentWidget(self.uic.mainCore)
        self.uic.Menu.setCurrentWidget(self.uic.MenuCore)
        self.uic.Module.setCurrentWidget(self.uic.ModuleCore)
        self.uic.progressBar.setValue(0)
        self.uic.nhapText.setText("")
        self.uic.nhapTextNumber.setText("")
        self.uic.Ok1.hide()
        self.uic.Ok2.hide()
        self.uic.OK3.hide()
        self.uic.huybo.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
