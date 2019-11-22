from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class Form(QWidget):
	def __init__(self):
		super(Form, self).__init__()
		self.setGeometry(50, 100, 800, 600)
		self.btn = QPushButton("welcome To Python Class", self)
		self.btn.move(100, 100)
		self.btn.clicked.connect(self.ptr_hello)

	def prt_hello(self):
		print(self.btn.text())

app = QApplication([])
form = Form()
form.show()
app.exec_()
