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
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(320, 520, 151, 81))
        self.button.setObjectName("button")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(130, 30, 571, 192))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 300, 511, 131))
        self.label.setObjectName("label")
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
        self.button.setText(_translate("MainWindow", "Button"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
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
