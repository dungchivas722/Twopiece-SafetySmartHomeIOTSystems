import sys
#import uu

from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from QtGui import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
# Khai bao code
    # tạo table với số hàng
        self.uic.tableWidget.setRowCount(10)
    # taoj table voi so cot
        self.uic.tableWidget.setColumnCount(4)
    # ghi len mot o bat ky
        self.uic.tableWidget.setItem(0,0,QTableWidgetItem("hello"))
    # khai bao nut them dong
        self.uic.button_themdong.clicked.connect(self.add_row)
    # khai bao nut xoa dong
        self.uic.button_xoadong.clicked.connect(self.remove_row)
    # khai bao nut them cot
        self.uic.button_themcot.clicked.connect(self.add_col)
    # khai bao nut xoa cot
        self.uic.buttom_xoacot.clicked.connect(self.remove_col)
    # sua dia chi ki tu o dong
        self.uic.tableWidget.setHorizontalHeaderLabels(['A1', 'A2', 'A3', 'A4', 'A5', 'A6'])

    # doc tu mot o bat ky
    def read_cell(self):
        try:
            a= self.uic.tableWidget.item(0,0).text()
            print(a)
        except:
            print("emty")

    #them dong
    def add_row(self):
        # them vi tri cuooi cung
        #row_bottom = self.uic.tableWidget.rowCount()
        # them vi tri bat ki
        current_row = self.uic.tableWidget.currentRow()

        self.uic.tableWidget.insertRow(current_row)

    #xoa dong
    def remove_row(self):
        # xoa vi tri cuoi cung
        # row_bottom = self.uic.tabl_eWidget.rowCount()
        # xoa vi tri hien tai
        current_row = self.uic.tableWidget.currentRow()

        self.uic.tableWidget.removeRow(current_row)

    #them cot
    def add_col(self):
        # them vi tri cuooi cung
        #col_bottom = self.uic.tableWidget.columnCount()
        # them vi tri bat ki
        current_Col = self.uic.tableWidget.currentColumn()

        self.uic.tableWidget.insertColumn(current_Col)

    #xoa cot
    def remove_col(self):
        # xoa vi tri cuoi cung
        # col_bottom = self.uic.tableWidget.columnCount()
        # xoa vi tri hien tai
        current_Col = self.uic.tableWidget.currentColumn()

        self.uic.tableWidget.removeColumn(current_Col)

    def show(self):
        # command to run
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
