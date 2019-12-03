import sys
from threading import Thread
from PyQt5.QtWidgets import QApplication

from pyqtconsole.console import PythonConsole


app = QApplication([])
console = PythonConsole()

#console.insert_input_text("hello", )
console.insert_input_text(text="hello")

console.show()

console.eval_queued()
#console.eval_in_thread()

sys.exit(app.exec_())