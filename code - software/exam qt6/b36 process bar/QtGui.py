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
        MainWindow.resize(1206, 720)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(60, 520, 191, 81))
        self.startButton.setObjectName("startButton")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(340, 520, 191, 81))
        self.clearButton.setObjectName("clearButton")
        self.removeButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeButton.setGeometry(QtCore.QRect(610, 520, 191, 81))
        self.removeButton.setObjectName("removeButton")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(170, 200, 621, 141))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1206, 21))
        self.menubar.setObjectName("menubar")
        self.menutoool = QtWidgets.QMenu(self.menubar)
        self.menutoool.setObjectName("menutoool")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionvcl = QtGui.QAction(MainWindow)
        self.actionvcl.setObjectName("actionvcl")
        self.actionvcl2 = QtGui.QAction(MainWindow)
        self.actionvcl2.setObjectName("actionvcl2")
        self.actionvcl3 = QtGui.QAction(MainWindow)
        self.actionvcl3.setObjectName("actionvcl3")
        self.menutoool.addAction(self.actionvcl)
        self.menutoool.addAction(self.actionvcl2)
        self.menutoool.addAction(self.actionvcl3)
        self.menubar.addAction(self.menutoool.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startButton.setText(_translate("MainWindow", "Bắt đầu"))
        self.clearButton.setText(_translate("MainWindow", "Xóa hết"))
        self.removeButton.setText(_translate("MainWindow", "Xóa 1 cái"))
        self.menutoool.setTitle(_translate("MainWindow", "toool"))
        self.actionvcl.setText(_translate("MainWindow", "vcl"))
        self.actionvcl2.setText(_translate("MainWindow", "vcl2"))
        self.actionvcl3.setText(_translate("MainWindow", "vcl3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
