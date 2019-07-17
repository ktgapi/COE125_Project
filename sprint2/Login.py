# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from SignUp import Sign_Up
import resources
from datalogic import DataLogic
index = 0

class Log_In(object):
    def SignWin(self):
        self.Swin = QtWidgets.QWidget()
        self.ui = Sign_Up()
        self.ui.setupUi(self.Swin)
        self.Swin.show()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.setEnabled(True)
        Form.resize(433, 503)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(433, 503))
        Form.setMaximumSize(QtCore.QSize(433, 503))
        Form.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Form.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Images/Images/User.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("*{\n"
"font-family:century-gotchic;\n"
"font-size:26px;\n"
"\n"
"}\n"
"#Form{\n"
"background-image: url(:/Images/Images/back.png);\n"
"}\n"
"QFrame\n"
"{\n"
"background:rgb(0,0,0,0.8);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton\n"
"{\n"
"color: rgb(46, 52, 54);\n"
"background:#0575A2;\n"
"border-radius:15px;\n"
"\n"
"}\n"
"QToolButton\n"
"{\n"
"background:#0575A2;\n"
"border-radius:40px;\n"
"\n"
"}\n"
"QLabel\n"
"{\n"
"    color: rgb(238, 238, 236);\n"
"\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"color:white;\n"
"background:rgb(50, 85, 162);\n"
"border-radius:15px;\n"
"\n"
"}\n"
"QLineEdit\n"
"{\n"
"font-family:century-gotchic;\n"
"font-size:20px;\n"
"background:transparent;\n"
"color:rgb(238, 238, 236);\n"
"border:none;\n"
"border-bottom:1px solid rgb(238, 238, 236); \n"
"}")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(60, 110, 311, 331))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.NextButton = QtWidgets.QPushButton(self.frame)
        self.NextButton.setGeometry(QtCore.QRect(80, 224, 151, 41))
        self.NextButton.setObjectName("NextButton")
        self.LineEdit = QtWidgets.QLineEdit(self.frame)
        self.LineEdit.setGeometry(QtCore.QRect(20, 130, 271, 31))
        self.LineEdit.setText("")
        self.LineEdit.setObjectName("LineEdit")
        self.RegButton = QtWidgets.QPushButton(self.frame)
        self.RegButton.setGeometry(QtCore.QRect(80, 270, 151, 41))
        self.RegButton.setObjectName("RegButton")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 100, 141, 31))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 271, 31))
        self.label_3.setStyleSheet("font: 63 12pt \"FreeSans\";\n"
"color: rgb(196, 152, 64);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(180, 60, 81, 81))
        self.toolButton.setText("")
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(120, 120))
        self.toolButton.setAutoRaise(False)
        self.toolButton.setObjectName("toolButton")
        self.NextButton.clicked.connect(self.login)
        self.RegButton.clicked.connect(self.SignWin)
        self.retranslateUi(Form)
        self.LineEdit.textChanged['QString'].connect(self.label_3.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.LineEdit, self.NextButton)
        Form.setTabOrder(self.NextButton, self.RegButton)
        Form.setTabOrder(self.RegButton, self.toolButton)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "App"))
        self.NextButton.setText(_translate("Form", "Next"))
        self.RegButton.setText(_translate("Form", "Register"))
        self.label.setText(_translate("Form", "Username"))


    def login(self): 
        Username = self.LineEdit.text()
        if self.UserCheck(Username) is False:
            if Username == '':
                self.label_3.setText("Empty Username")
            else:
                self.label_3.setText("Incorrect Username")
        else:
            self.RegButton.hide()
            self.label.setText("Password")
            self.LineEdit.clear()     
            self.LineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
            self.NextButton.setText("Login")
            self.NextButton.clicked.disconnect(self.login)
            self.NextButton.clicked.connect(self.PassCheck) 
    def UserCheck(self,username):
        found = dl.isUserExist(username)
        return found
    def PassCheck(self):
        pw = self.LineEdit.text()
        mess = dl.isMatch(pw)
        if (mess == "Incorrect Password"):
            self.label_3.setText(mess)      
        else:
            self.label_3.setText("Welcome "+ mess)


if __name__ == "__main__":
    import sys
    dl = DataLogic()
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Log_In()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

