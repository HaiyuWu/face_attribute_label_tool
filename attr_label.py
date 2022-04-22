import sys
from utils.qt import *
from PySide2 import QtCore
from PySide2.QtWidgets import QApplication


QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


app = QApplication(sys.argv)
ui_file = resource_path("myUI.ui")
root_file = resource_path("root.txt")
ui = MyUI(ui_file, root_file)
app.exec_()
