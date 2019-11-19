import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(500, 200, 550, 400)
        self.setWindowTitle("Passwod Crack")

        oImage = QImage("anonymous.jpeg")
        sImage = oImage.scaled(QSize(550, 400))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

        self.pushButton = QPushButton("파일 찾기")
        self.lineEdit = QLineEdit()
        self.pushButton.clicked.connect(self.pushButtonClicked)
        self.label = QLabel("파일경로")

        layout = QHBoxLayout()
        layout.addWidget(self.pushButton)
        layout.addWidget(self.label)
        layout.addWidget(self.lineEdit)

        self.setLayout(layout)

    def pushButtonClicked(self):
        fname = QFileDialog.getOpenFileName(self)
        self.label.setText(fname[0])

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()