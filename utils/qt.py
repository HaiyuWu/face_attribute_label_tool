from PySide2 import QtWidgets
from PySide2.QtUiTools import *
from utils.operation import Operation
import os


class MyUI(QtWidgets.QMainWindow):
    def __init__(self, ui_file, parent=None):
        super(MyUI, self).__init__(parent=parent)
        # load ui file
        self.ui = QUiLoader().load(ui_file, self)
        # open image
        self.operation = Operation(self.ui)
        self.setMinimumWidth(677)
        self.setMinimumHeight(590)
        self.show()

    def closeEvent(self, event):
        try:
            self.operation.save()
        except Exception:
            pass
        names = self.operation.isleft()
        if names:
            result = QtWidgets.QMessageBox.question(self, "Quit message",
                                                    "Do you want to quit Without completing the unfinished labels?",
                                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if result == QtWidgets.QMessageBox.Yes:
                self.delete(names)
                pass
            else:
                event.ignore()

    def delete(self, names):
        for label, uncertain in names:
            os.remove(label)
            os.remove(uncertain)
