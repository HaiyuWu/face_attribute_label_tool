from PySide2 import QtWidgets, QtCore


class LabelCollector(object):
    def __init__(self, ui):
        self.ui = ui
        self.label_buttons = {}
        self.occluded_buttons = {}
        self.names = {}
        for name, value in vars(self.ui).items():
            if isinstance(value, QtWidgets.QButtonGroup):
                self.label_buttons[name] = value
            if isinstance(value, QtWidgets.QCheckBox):
                self.occluded_buttons[name] = value

        self.label_buttons = sorted(self.label_buttons.items(), key=lambda x: int(x[0].split("_")[-1]))

        self.labels = [-1] * 40
        for index, (_, value) in enumerate(self.label_buttons):
            value.buttonClicked.connect(lambda value, index=index: self.collect(value, index, "label"))

        self.occluded = [0] * 40
        for index, (_, value) in enumerate(self.occluded_buttons.items()):
            value.clicked.connect(lambda value=value, index=index: self.collect(value, index, "occluded"))

    def collect(self, button, index, which_list):
        if which_list == "label":
            self.labels[index] = int(button.text())
        elif which_list == "occluded":
            if button.checkState() == QtCore.Qt.CheckState.Unchecked:
                self.occluded[index] = 0
            else:
                self.occluded[index] = 1
        # print(self.labels)

    def button_init(self, labels, occludeds):
        for index, ((_, label_button), (_, occluded_button)) in enumerate(
                zip(self.label_buttons, self.occluded_buttons.items())):
            label_button.setExclusive(False)
            for j, btn in enumerate(label_button.buttons()):
                if labels[index] != -1 and labels[index] == j:
                    btn.setChecked(True)
                else:
                    btn.setChecked(False)
            occluded_button.setChecked(occludeds[index] == 1)
            label_button.setExclusive(True)

    def label_list(self):
        return self.labels

    def occluded_list(self):
        return self.occluded

    def set_lists(self, label_list, occluded_list):
        self.labels = label_list
        self.occluded = occluded_list
        self.button_init(label_list, occluded_list)

    def isfinished(self):
        return bool(-1 not in self.labels)
