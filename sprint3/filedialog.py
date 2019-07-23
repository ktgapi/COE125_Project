import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
import shutil
import os.path

class file_browse(QWidget):
    got_filename = QtCore.pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.fn = ""
    
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Select an Image", "","Image Files (*.jpg *.jpeg *.png *.tif *.tiff *.bmp)", options=options)
        if fileName:
            print(fileName)
            self.fn = fileName
            self.got_filename.emit(self.fn)
        shutil.copy2(fileName,"./images/sub")
        
 
