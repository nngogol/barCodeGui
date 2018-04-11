from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from untitled import *
import os
import sys

import barcode
from barcode import generate
from barcode.writer import ImageWriter
import datetime


def getNameForFile():
    return str(datetime.datetime.today()).replace(':', '-').replace('.', '-')

class MyWin(QtWidgets.QMainWindow):
    version = '1.0'

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Bar code manager ' + self.version)

        if not os.path.exists(os.getcwd() + "\\results bars"):
            os.mkdir(os.getcwd() + "\\results bars")

        # btns bind
        self.ui.mkbar_svg.clicked.connect(self.mkbar_svg_h)
        self.ui.mkbar_png.clicked.connect(self.mkbar_png_h)
        self.ui.open_res.clicked.connect(lambda : os.startfile(os.getcwd() + "\\results bars"))

        # add all avaibles codes
        self.ui.barcombo.addItems([str(i) for i in barcode.PROVIDED_BARCODES])


    def mbox(self, body, title='Erroe'):
        dialog = QMessageBox(QMessageBox.Information, title, body)
        dialog.exec_()

    def mkbar_svg_h(self):
        try:
            type_of_bar = self.ui.barcombo.currentText()
            payload = self.ui.payload.text()
            where_to_save = getNameForFile()
            noBarText = not self.ui.noBarText.isChecked()

            if self.ui.rad_name.isChecked():
                where_to_save = self.ui.fname.text()

            name = generate(type_of_bar,
                            payload,
                            output='results bars/' + where_to_save,
                            writer_options={'write_text': noBarText})
        
        except Exception as e:
            self.mbox(str(e))


    def mkbar_png_h(self):
        try:
            type_of_bar = self.ui.barcombo.currentText()
            payload = self.ui.payload.text()
            where_to_save = getNameForFile()
            noBarText = not self.ui.noBarText.isChecked()

            if self.ui.rad_name.isChecked():
                where_to_save = self.ui.fname.text()

        
            needed_bar_class = barcode.get_barcode_class(type_of_bar)
            mybarcode = needed_bar_class(payload, writer=ImageWriter())
            fullname = mybarcode.save('results bars/' + where_to_save, options={'write_text': noBarText})

        except Exception as e:
            self.mbox(str(e))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
