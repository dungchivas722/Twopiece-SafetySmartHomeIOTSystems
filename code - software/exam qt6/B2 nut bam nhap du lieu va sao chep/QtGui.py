# Form implementation generated from reading ui file 'pyqt.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        font = QtGui.QFont()
        font.setPointSize(26)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_saochep = QtWidgets.QPushButton(self.centralwidget)
        self.button_saochep.setGeometry(QtCore.QRect(180, 470, 181, 71))
        self.button_saochep.setObjectName("button_saochep")
        self.button_ketthuc = QtWidgets.QPushButton(self.centralwidget)
        self.button_ketthuc.setGeometry(QtCore.QRect(780, 470, 201, 91))
        self.button_ketthuc.setObjectName("button_ketthuc")
        self.screen = QtWidgets.QLabel(self.centralwidget)
        self.screen.setGeometry(QtCore.QRect(470, 30, 231, 151))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.screen.setFont(font)
        self.screen.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.screen.setObjectName("screen")
        self.screen_text = QtWidgets.QTextEdit(self.centralwidget)
        self.screen_text.setGeometry(QtCore.QRect(300, 270, 581, 71))
        self.screen_text.setObjectName("screen_text")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 53))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_saochep.setText(_translate("MainWindow", "Copy"))
        self.button_ketthuc.setText(_translate("MainWindow", "Dung"))
        self.screen.setText(_translate("MainWindow", "XIN LUI dc chua"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
