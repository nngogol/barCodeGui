# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(407, 375)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mkbar_svg = QtWidgets.QPushButton(self.centralwidget)
        self.mkbar_svg.setGeometry(QtCore.QRect(270, 260, 121, 23))
        self.mkbar_svg.setObjectName("mkbar_svg")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 221, 71))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.payload = QtWidgets.QLineEdit(self.groupBox)
        self.payload.setObjectName("payload")
        self.verticalLayout_3.addWidget(self.payload)
        self.noBarText = QtWidgets.QCheckBox(self.centralwidget)
        self.noBarText.setGeometry(QtCore.QRect(220, 120, 131, 41))
        self.noBarText.setObjectName("noBarText")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 110, 181, 131))
        self.groupBox_2.setObjectName("groupBox_2")
        self.rad_random = QtWidgets.QRadioButton(self.groupBox_2)
        self.rad_random.setGeometry(QtCore.QRect(60, 20, 61, 18))
        self.rad_random.setChecked(True)
        self.rad_random.setObjectName("rad_random")
        self.rad_name = QtWidgets.QRadioButton(self.groupBox_2)
        self.rad_name.setGeometry(QtCore.QRect(60, 70, 71, 18))
        self.rad_name.setObjectName("rad_name")
        self.fname = QtWidgets.QLineEdit(self.groupBox_2)
        self.fname.setEnabled(False)
        self.fname.setGeometry(QtCore.QRect(30, 100, 131, 20))
        self.fname.setObjectName("fname")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setEnabled(False)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 250, 181, 51))
        self.groupBox_3.setObjectName("groupBox_3")
        self.ftype = QtWidgets.QComboBox(self.groupBox_3)
        self.ftype.setGeometry(QtCore.QRect(50, 20, 74, 22))
        self.ftype.setObjectName("ftype")
        self.ftype.addItem("")
        self.ftype.addItem("")
        self.ftype.addItem("")
        self.mkbar_png = QtWidgets.QPushButton(self.centralwidget)
        self.mkbar_png.setGeometry(QtCore.QRect(270, 290, 121, 23))
        self.mkbar_png.setObjectName("mkbar_png")
        self.open_res = QtWidgets.QPushButton(self.centralwidget)
        self.open_res.setGeometry(QtCore.QRect(270, 320, 121, 23))
        self.open_res.setObjectName("open_res")
        self.groupbox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupbox.setGeometry(QtCore.QRect(250, 10, 151, 71))
        self.groupbox.setObjectName("groupbox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupbox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.groupbox)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.barcombo = QtWidgets.QComboBox(self.groupbox)
        self.barcombo.setObjectName("barcombo")
        self.verticalLayout.addWidget(self.barcombo)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 407, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.rad_name.toggled['bool'].connect(self.fname.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mkbar_svg.setText(_translate("MainWindow", "Make barcode in SVG"))
        self.label_3.setText(_translate("MainWindow", "Text to encode"))
        self.noBarText.setText(_translate("MainWindow", "I want to \n"
"remove barcode text\n"
"from image"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Filename"))
        self.rad_random.setText(_translate("MainWindow", "random"))
        self.rad_name.setText(_translate("MainWindow", "set name"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Filetype"))
        self.ftype.setItemText(0, _translate("MainWindow", "svg"))
        self.ftype.setItemText(1, _translate("MainWindow", "png"))
        self.ftype.setItemText(2, _translate("MainWindow", "jpg"))
        self.mkbar_png.setText(_translate("MainWindow", "Make barcode in PNG"))
        self.open_res.setText(_translate("MainWindow", "Open results folder"))
        self.label.setText(_translate("MainWindow", "barcode type"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

