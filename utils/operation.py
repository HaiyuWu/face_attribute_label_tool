from utils.label_collection import LabelCollector
from utils.im_show import ImShow
from PySide2.QtWidgets import *
from PySide2 import QtCore
from glob import glob
import os
import numpy as np


# next, prev, open
class Operation(object):
    def __init__(self, ui, root):
        self.ui = ui
        self.image_path = None
        self.im_list = None
        self.old_path = None
        self.directory = None
        self.current_index = None
        self.image_name = ""
        self.lcollector = None
        self.not_finished = []
        self.save_path = ""
        self.open_root = self._get_root(root)
        self.name_label = self.ui.ImageName
        # open an image
        self.open_image = self.ui.OpenImg.clicked.connect(self.open_image)
        # collect results from input
        # next image
        self.next_image = self.ui.NextImg.clicked.connect(lambda: self._op("next"))
        self.prev_image = self.ui.PrevImg.clicked.connect(lambda: self._op("prev"))

    def _get_root(self, path):
        with open(path, "r") as f:
            root = f.read()
        return root

    def get_root(self):
        return self.open_root

    def open_image(self):
        self.image_path, _ = QFileDialog.getOpenFileName(self.ui, "Choose an image", rf"{self.open_root}",
                                                         "types(*.png *.jpg *.bmp *.JPG *.PNG)")
        if self.image_path:
            self.directory = os.path.abspath(os.path.join(self.image_path, os.pardir))
            self.open_root = self.directory
            self.save_path = self.directory + "/results/"
            if not os.path.exists(self.save_path):
                os.makedirs(self.save_path)

            self.im_list = glob(
                 self.directory + f"/*.{self.image_path.split('.')[-1]}")
            self.lcollector = LabelCollector(self.ui)
            self.im_list = self._clean_path()
            self.current_index = self.im_list.index(self.image_path)
            self._show()

    def _clean_path(self):
        return list(map(lambda x: x.replace("\\", "/"), self.im_list))

    def _op(self, status):
        if self.im_list:
            if status == "next" and self.current_index < len(self.im_list) - 1:
                self.current_index += 1
            elif status == "prev" and self.current_index > 0:
                self.current_index -= 1

            self.save()
            self.image_path = self.im_list[self.current_index]
            self._show()

    def _get_im_name(self):
        self.image_name = self.image_path.split('/')[-1].split('.')[0]

    def isleft(self):
        # print(self.not_finished)
        return self.not_finished

    def _show(self):
        ImShow(self.ui, self.image_path)
        self._get_im_name()
        self.name_label.setText(self.image_name)
        self.name_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.reset()

    def save(self):
        label, uncertain = self.lcollector.label_list(), self.lcollector.uncertain_list()
        if sum(label) != -40:
            image_name = self.image_name
            npy_label_file = f"{self.save_path}{image_name}_label.npy"
            npy_uncertain_file = f"{self.save_path}{self.image_path.split('/')[-1].split('.')[0]}_uncertain.npy"
            # print(label)
            np.save(npy_label_file, label)
            np.save(npy_uncertain_file, uncertain)

    def reset(self):
        npys = os.listdir(self.save_path)
        target_label = f"{self.image_name}_label.npy"
        target_uncertain = f"{self.image_name}_uncertain.npy"
        if target_label not in npys:
            labels = [-1] * 40
            uncertains = [0] * 40
            image_name = self.image_name
            npy_label_file = f"{self.save_path}{image_name}_label.npy"
            npy_uncertain_file = f"{self.save_path}{image_name}_uncertain.npy"
            self.not_finished.append((npy_label_file, npy_uncertain_file))
        else:
            labels = np.load(self.save_path + target_label)
            uncertains = np.load(self.save_path + target_uncertain)
        self.lcollector.set_lists(labels, uncertains)


