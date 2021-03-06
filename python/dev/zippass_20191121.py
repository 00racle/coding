import sys
import subprocess
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
        '''
        #oImage = QImage("anony.png")
        oImage = QImage("anonyback.jpg")
        sImage = oImage.scaled(QSize(600, 450))
        #sImage = oImage.scaled(QSize(50, 25))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)
        '''

        self.pushButton01 = QPushButton("파일 찾기")
        #self.pushButton01.move(20, 20)
        self.pushButton02 = QPushButton("Start Crack")
        self.lineEdit = QLineEdit()
        self.pushButton01.clicked.connect(self.pushButtonClicked)
        self.pushButton02.clicked.connect(self.startCracked)
        self.label = QLabel("파일경로")

        #uplayout 에 이미지 삽입
        self.imglabel = QLabel()
        #pixmap = QPixmap("anonyback.jpg")
        pixmap = QPixmap("anonymous.jpeg")
        self.imglabel.setPixmap(pixmap)

        #self.rettext = QTextEdit()
        self.output = QLineEdit()
        self.lcd = QLCDNumber()
        self.lcd.setFixedHeight(100)

        upLayout = QVBoxLayout()
        downLayout = QVBoxLayout()
        downLayout.addWidget(self.pushButton01)
        downLayout.addWidget(self.lineEdit)
        downLayout.addWidget(self.pushButton02)
        #downLayout.addWidget(self.rettext)
        downLayout.addWidget(self.lcd)
        upLayout.addWidget(self.imglabel)

        layout = QVBoxLayout()
        layout.addLayout(upLayout)
        layout.addLayout(downLayout)

        self.setLayout(layout)

    def pushButtonClicked(self):
        fname = QFileDialog.getOpenFileName(self)
        #self.label.setText(fname[0])
        self.filename = fname[0]
        self.lineEdit.setText(fname[0])

    '''
    def startCracked(self):
        for i in range(100):
            self.lcd.display(i)
            self.lcd.repaint()
            time.sleep(0.01)
            #self.rettext.setText(str(i))
    '''
    def startCracked(self):
        subprocess.Popen(["/usr/bin/open", "-n", "-a", "/Applications/iTerm.app/Contents/MacOS/iTerm2", "--args", \
                          '/Users/ORACLE/testenv/bin/python3 /Users/ORACLE/testenv/envdir/git/coding/python/dev/hello.py'])

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
