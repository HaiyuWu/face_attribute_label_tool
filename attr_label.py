import sys
from utils.qt import *
from PySide2.QtWidgets import QApplication


app = QApplication(sys.argv)
ui_file = os.getcwd() + "/utils/myUI.ui"
ui = MyUI(ui_file)
app.exec_()
