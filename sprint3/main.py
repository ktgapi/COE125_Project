# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
import os, shutil
from filedialog import file_browse

folder = './images/sub'

class Main_Program(object):
    def setupUi(self, MainWindow):
        self.FileName = ""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 409)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/card.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(107, 126, 130);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Kozuka Gothic Pr6N B\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pb_Browse = QtWidgets.QPushButton(self.centralwidget)
        self.pb_Browse.setGeometry(QtCore.QRect(10, 260, 101, 25))
        self.pb_Browse.setStyleSheet("background-color: rgb(132, 181, 195);\n"
"color: rgb(255, 255, 255);")
        self.pb_Browse.setObjectName("pb_Browse")
        self.pb_Evaluate = QtWidgets.QPushButton(self.centralwidget)
        self.pb_Evaluate.setGeometry(QtCore.QRect(290, 260, 101, 25))
        self.pb_Evaluate.setStyleSheet("background-color: rgb(132, 181, 195);\n"
"color: rgb(255, 255, 255);")
        self.pb_Evaluate.setObjectName("pb_Evaluate")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 121, 17))
        self.label.setObjectName("label")
        self.lbl_Name = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Name.setGeometry(QtCore.QRect(410, 0, 381, 20))
        self.lbl_Name.setText("")
        self.lbl_Name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_Name.setObjectName("lbl_Name")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 300, 191, 17))
        self.label_2.setObjectName("label_2")
        self.pb_Generate = QtWidgets.QPushButton(self.centralwidget)
        self.pb_Generate.setGeometry(QtCore.QRect(10, 330, 101, 25))
        self.pb_Generate.setStyleSheet("background-color: rgb(132, 181, 195);\n"
"color: rgb(255, 255, 255);")
        self.pb_Generate.setObjectName("pb_Generate")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 381, 211))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_3.setScaledContents(True)
        self.pb_Generate.clicked.connect(self.generateDigit)
        self.pb_Evaluate.clicked.connect(self.evaluateImage)
        self.pb_Browse.clicked.connect(self.browseImage)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Digit Recognition"))
        self.pb_Browse.setText(_translate("MainWindow", "Browse"))
        self.pb_Evaluate.setText(_translate("MainWindow", "Evaluate"))
        self.label.setText(_translate("MainWindow", "Browse an Image"))
        self.label_2.setText(_translate("MainWindow", "Evaluate from sample data"))
        self.pb_Generate.setText(_translate("MainWindow", "Generate"))

    def generateDigit(self):
        import businesslogic
        businesslogic.testFromDataSet()

    def evaluateImage(self):
        import businesslogic
        businesslogic.testFromUserInput()


    def browseImage(self):
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)
        fb = file_browse()
        fb.openFileNameDialog()
        pixmap = QPixmap(fb.fn)
        print(pixmap)
        self.label_3.setPixmap(pixmap)
        
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Main_Program()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
