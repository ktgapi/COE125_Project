import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
import shutil
import os.path
import main

class file_browse(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.openFileNameDialog()
    
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Select an Image", "","Image Files (*.jpg *.jpeg *.png *.tif *.tiff *.bmp)", options=options)
        if fileName:
            print(fileName)
        shutil.copy2(fileName,"./images/sub")
        Main_Program.label_3.setPixmap(fileName)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
