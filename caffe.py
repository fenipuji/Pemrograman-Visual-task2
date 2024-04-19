# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'caffe.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import image_qrc, sys

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 370)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 371, 341))
        self.label.setStyleSheet("border-image: url(:/image/foto caffe.jpeg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(130, 160, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.spinBox_2 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(130, 190, 111, 22))
        self.spinBox_2.setMinimum(2)
        self.spinBox_2.setMaximum(50)
        self.spinBox_2.setObjectName("spinBox_2")
        self.comboBox_4 = QtWidgets.QComboBox(Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(130, 220, 111, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 130, 111, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 250, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(62)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(30, 127, 255);\n"
"    border-radius: 10px;\n"
"    color:#ffffff;\n"
"    font-size:15px;\n"
"    font-weight:500;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(180, 181, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(30, 127, 255); */\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(30, 127, 255);\n"
"    border-radius: 10px;\n"
"    color:#ffffff;\n"
"    font-size:15px;\n"
"    font-weight:500;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(180, 181, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(30, 127, 255); */\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(120, 100, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(255, 255, 255);\n"
"")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "Americano"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "Cappucino"))
        self.comboBox_3.setItemText(2, _translate("Dialog", "Caramel latte"))
        self.comboBox_3.setItemText(3, _translate("Dialog", "Black tea"))
        self.comboBox_4.setItemText(0, _translate("Dialog", "Kecil"))
        self.comboBox_4.setItemText(1, _translate("Dialog", "Jumbo"))
        self.pushButton.setText(_translate("Dialog", "Buat Pesanan"))
        self.label_2.setText(_translate("Dialog", "Mulai Memesan"))
import image_qrc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
