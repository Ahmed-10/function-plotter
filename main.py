import sys
from PySide2.QtWidgets import QApplication
from view import WinView

app = QApplication([])

widget = WinView()
sys.exit(app.exec_())