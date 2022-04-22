from PySide2 import QtWidgets, QtCore


class LabelCollector(object):
    def __init__(self, ui):
        self.ui = ui
        self.label_buttons = {}
        self.uncertain_buttons = {}
        self.names = {}
        for name, value in vars(self.ui).items():
            if isinstance(value, QtWidgets.QButtonGroup):
                self.label_buttons[name] = value
            if isinstance(value, QtWidgets.QCheckBox):
                self.uncertain_buttons[name] = value

        self.label_buttons = sorted(self.label_buttons.items(), key=lambda x: int(x[0].split("_")[-1]))

        self.labels = [-1] * 40
        for index, (_, value) in enumerate(self.label_buttons):
            value.buttonClicked.connect(lambda value, index=index: self.collect(value, index, "label"))

        self.uncertain = [0] * 40
        for index, (_, value) in enumerate(self.uncertain_buttons.items()):
            value.clicked.connect(lambda value=value, index=index: self.collect(value, index, "uncertain"))

    def collect(self, button, index, which_list):
        if which_list == "label":
            self.labels[index] = int(button.text())
        elif which_list == "uncertain":
            if button.checkState() == QtCore.Qt.CheckState.Unchecked:
                self.uncertain[index] = 0
            else:
                self.uncertain[index] = 1
        # print(self.labels)

    def button_init(self, labels, uncertains):
        for index, ((_, label_button), (_, uncertain_button)) in enumerate(
                zip(self.label_buttons, self.uncertain_buttons.items())):
            label_button.setExclusive(False)
            for j, btn in enumerate(label_button.buttons()):
                if labels[index] != -1 and labels[index] == j:
                    btn.setChecked(True)
                else:
                    btn.setChecked(False)
            uncertain_button.setChecked(uncertains[index] == 1)
            label_button.setExclusive(True)

    def label_list(self):
        return self.labels

    def uncertain_list(self):
        return self.uncertain

    def set_lists(self, label_list, uncertain_list):
        self.labels = label_list
        self.uncertain = uncertain_list
        self.button_init(label_list, uncertain_list)

    def isfinished(self):
        return bool(-1 not in self.labels)
