from utils.label_collection import LabelCollector
from utils.im_show import ImShow
from PySide2.QtWidgets import *
from PySide2 import QtCore
from glob import glob
import os
import numpy as np


# next, prev, open
class Operation(object):
    def __init__(self, ui, last_path):
        self.ui = ui
        self.image_path = None
        self.im_list = None
        self.old_path = None
        self.directory = None
        self.last_path = last_path
        self.current_index = None
        self.image_name = ""
        self.lcollector = None
        self.not_finished = []
        self.save_path = ""
        self.name_label = self.ui.ImageName
        # open an image
        self.open_image = self.ui.OpenImg.clicked.connect(self.open_image)
        # collect results from input
        # next image
        self.next_image = self.ui.NextImg.clicked.connect(lambda: self.op("next"))
        self.prev_image = self.ui.PrevImg.clicked.connect(lambda: self.op("prev"))

    def get_dir(self):
        return self.directory

    def open_image(self):
        self.image_path, _ = QFileDialog.getOpenFileName(self.ui, "Choose an image", rf"{self.last_path}",
                                                         "types(*.png *.jpg *.bmp *.JPG *.PNG)")
        if self.image_path:
            self.directory = os.path.abspath(os.path.join(self.image_path, os.pardir))
            self.save_path = self.directory + "/results/"
            if not os.path.exists(self.save_path):
                os.makedirs(self.save_path)

            self.im_list = glob(
                 self.directory + f"/*.{self.image_path.split('.')[-1]}")
            # fixed the order bug on IOS platform
            self.im_list.sort()
            self.lcollector = LabelCollector(self.ui)
            self.im_list = self._clean_path()
            self.current_index = self.im_list.index(self.image_path)
            self._show()

    def _clean_path(self):
        return list(map(lambda x: x.replace("\\", "/"), self.im_list))

    def op(self, status):
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
        label, occluded = self.lcollector.label_list(), self.lcollector.occluded_list()
        if sum(label) != -40:
            image_name = self.image_name
            npy_label_file = f"{self.save_path}{image_name}_label.npy"
            npy_occluded_file = f"{self.save_path}{self.image_path.split('/')[-1].split('.')[0]}_occluded.npy"
            # print(label)
            np.save(npy_label_file, label)
            np.save(npy_occluded_file, occluded)

    def reset(self):
        npys = os.listdir(self.save_path)
        target_label = f"{self.image_name}_label.npy"
        target_occluded = f"{self.image_name}_occluded.npy"
        if target_label not in npys:
            labels = [-1] * 40
            occludeds = [0] * 40
            image_name = self.image_name
            npy_label_file = f"{self.save_path}{image_name}_label.npy"
            npy_occluded_file = f"{self.save_path}{image_name}_occluded.npy"
            np.save(npy_label_file, labels)
            np.save(npy_occluded_file, occludeds)
            self.not_finished.append((npy_label_file, npy_occluded_file))
        else:
            labels = np.load(self.save_path + target_label)
            try:
                occludeds = np.load(self.save_path + target_occluded)
            except Exception:
                occludeds = [0] * 40
                np.save(self.save_path + target_occluded, occludeds)
        self.lcollector.set_lists(labels, occludeds)


