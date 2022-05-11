from PySide2 import QtWidgets
from PySide2.QtCore import *
from PySide2.QtUiTools import *
from utils.operation import Operation
import os
# If you want to pack it on IOS system, just uncomment this line.
# os.environ['QT_MAC_WANTS_LAYER'] = '1'


class MyUI(QtWidgets.QMainWindow):
    def __init__(self, ui_file):
        super(MyUI, self).__init__()
        # load ui file
        # print(ui_file)
        self.ui = QUiLoader().load(ui_file, self)
        # open image
        self.operation = Operation(self.ui)
        self.setMinimumWidth(677)
        self.setMinimumHeight(590)
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_A:
            self.operation.op("prev")
        if event.key() == Qt.Key_D:
            self.operation.op("next")

    def closeEvent(self, event):
        try:
            self.operation.save()
        except Exception:
            pass
        names = self.operation.isleft()
        if names:
            result = QtWidgets.QMessageBox.question(self, "Quit message",
                                                    "You have uncompleted annotations. "
                                                    "Do you want to save the label anyway?",
                                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No |
                                                    QtWidgets.QMessageBox.Cancel)
            if result == QtWidgets.QMessageBox.Yes:
                pass
            elif result == QtWidgets.QMessageBox.No:
                self.delete(names)
            elif result == QtWidgets.QMessageBox.Cancel:
                event.ignore()

    def delete(self, names):
        for label, uncertain in names:
            os.remove(label)
            os.remove(uncertain)
