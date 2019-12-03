import sys
import subprocess
import zipfile
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QIcon, QPixmap

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.filename = ''

    def setupUI(self):
        self.setGeometry(500, 200, 600, 450)
        self.setWindowTitle("Passwod Crack")
        self.setWindowIcon(QIcon('anony.png'))

        self.pushButton01 = QPushButton("파일 찾기")
        self.pushButton02 = QPushButton("Start Crack")
        self.lineEdit = QLineEdit()
        self.pushButton01.clicked.connect(self.pushButtonClicked)
        self.pushButton02.clicked.connect(self.startCracked)
        self.label = QLabel("파일경로")

        #uplayout 에 이미지 삽입
        self.imglabel = QLabel()
        pixmap = QPixmap("anonymous.jpeg")
        self.imglabel.setPixmap(pixmap)

        #self.output = QLineEdit()
        self.lcd = QLCDNumber()
        self.lcd.setFixedHeight(100)

        upLayout = QVBoxLayout()
        downLayout = QVBoxLayout()
        downLayout.addWidget(self.pushButton01)
        downLayout.addWidget(self.lineEdit)
        downLayout.addWidget(self.pushButton02)
        downLayout.addWidget(self.lcd)
        upLayout.addWidget(self.imglabel)

        layout = QVBoxLayout()
        layout.addLayout(upLayout)
        layout.addLayout(downLayout)
        self.setLayout(layout)

    def crackzip(self, zfile, password):
        try:
            zfile.extractall(pwd = password.encode())
            return True
        except:
            pass

    def pushButtonClicked(self):
        fname = QFileDialog.getOpenFileName(self)
        self.filename = fname[0]
        self.lineEdit.setText(fname[0])


    def startCracked(self):
        zfile = zipfile.ZipFile(self.filename, 'r')
        for i in range(5000):
            self.lcd.display(i)
            self.lcd.repaint()
            time.sleep(0.005)
            if self.crackzip(zfile, str(i)) == True:
                break

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
