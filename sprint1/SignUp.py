# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignUp.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import resources
from datalogic import DataLogic

class Sign_Up(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.setEnabled(True)
        Form.resize(593, 482)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(593, 482))
        Form.setMaximumSize(QtCore.QSize(593, 482))
        Form.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Form.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Images/Images/User.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("*{\n"
"font-family:century-gotchic;\n"
"font-size:20px;\n"
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
"background:#DC3D3D;\n"
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
"background:transparent;\n"
"color:rgb(238, 238, 236);\n"
"border:none;\n"
"border-bottom:1px solid rgb(238, 238, 236); \n"
"}")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(100, 80, 411, 391))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.FNlabel = QtWidgets.QLabel(self.frame)
        self.FNlabel.setGeometry(QtCore.QRect(0, 60, 111, 51))
        self.FNlabel.setObjectName("FNlabel")
        self.Ulabel = QtWidgets.QLabel(self.frame)
        self.Ulabel.setGeometry(QtCore.QRect(0, 120, 111, 51))
        self.Ulabel.setObjectName("Ulabel")
        self.PLabel = QtWidgets.QLabel(self.frame)
        self.PLabel.setGeometry(QtCore.QRect(0, 180, 111, 51))
        self.PLabel.setObjectName("PLabel")
        self.Conlabel = QtWidgets.QLabel(self.frame)
        self.Conlabel.setGeometry(QtCore.QRect(0, 240, 191, 51))
        self.Conlabel.setObjectName("Conlabel")
        self.SignUpButton = QtWidgets.QPushButton(self.frame)
        self.SignUpButton.setGeometry(QtCore.QRect(130, 330, 141, 31))
        self.SignUpButton.setObjectName("SignUpButton")
        self.FNLine = QtWidgets.QLineEdit(self.frame)
        self.FNLine.setGeometry(QtCore.QRect(120, 70, 211, 25))
        self.FNLine.setObjectName("FNLine")
        self.Uline = QtWidgets.QLineEdit(self.frame)
        self.Uline.setGeometry(QtCore.QRect(120, 130, 211, 25))
        self.Uline.setObjectName("Uline")
        self.Pline = QtWidgets.QLineEdit(self.frame)
        self.Pline.setGeometry(QtCore.QRect(120, 190, 211, 25))
        self.Pline.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Pline.setObjectName("Pline")
        self.ConPassLine = QtWidgets.QLineEdit(self.frame)
        self.ConPassLine.setGeometry(QtCore.QRect(190, 250, 211, 25))
        self.ConPassLine.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ConPassLine.setObjectName("ConPassLine")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(0, 290, 401, 24))
        self.label_5.setStyleSheet("font: 63 12pt \"FreeSans\";\n"
"color: rgb(196, 152, 64);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(250, 40, 81, 81))
        self.toolButton.setText("")
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(120, 120))
        self.toolButton.setAutoRaise(False)
        self.toolButton.setObjectName("toolButton")
        self.SignUpButton.clicked.connect(self.Reg)
        self.retranslateUi(Form)
        self.Uline.textChanged['QString'].connect(self.label_5.clear)
        self.Pline.textChanged['QString'].connect(self.label_5.clear)
        self.FNLine.textChanged['QString'].connect(self.label_5.clear)
        self.ConPassLine.textChanged['QString'].connect(self.label_5.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.Dl = DataLogic()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "App"))
        self.FNlabel.setText(_translate("Form", "Full Name: "))
        self.Ulabel.setText(_translate("Form", "Username:"))
        self.PLabel.setText(_translate("Form", "Password:"))
        self.Conlabel.setText(_translate("Form", "Confrim Password:"))
        self.SignUpButton.setText(_translate("Form", "Sign Up"))

    def Reg(self):
         fullname = self.FNLine.text()
         if fullname.isspace() is True or fullname == "":
            self.label_5.setText("Name not found! Try again")
         else:
             username = self.Uline.text()
             if username.isspace() is True or self.UserCheck(username) is True or username == "":
                 self.label_5.setText("Username Invalid or exists. Try again")
             else:
                 password = self.Pline.text()
                 password2 = self.ConPassLine.text()
                 if password != password2 or password.isspace() is True or password == "":
                     self.label_5.setText("Passwords invalid or do not match! Try again")
                 else:
                    self.Dl.insertData(username, password, fullname)
                    self.label_5.setText("Registration Successful")
    def UserCheck (self, Username):
        found = self.Dl.isUserExist(Username)
        return found

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Sign_Up()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

