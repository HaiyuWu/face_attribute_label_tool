from PySide2 import QtWidgets
from PySide2.QtUiTools import *
from utils.operation import Operation
import os
# If you want to pack it on IOS system, just uncomment this line.
# os.environ['QT_MAC_WANTS_LAYER'] = '1'


class MyUI(QtWidgets.QMainWindow):
    def __init__(self, ui_file, parent=None):
        super(MyUI, self).__init__(parent=parent)
        # load ui file
        print(ui_file)
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
                                                    "You have some uncompleted annotations! "
                                                    "They will be discarded if the window is closed. "
                                                    "Do you still want to close the window?",
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
