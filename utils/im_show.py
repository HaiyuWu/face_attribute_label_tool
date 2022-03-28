from PySide2 import QtGui


class ImShow(object):
    def __init__(self, ui, im_path):
        # pixel area
        self.ui = ui
        self.im_path = im_path
        self.image_show = self.ui.images
        self._show_image()

    def _show_image(self):
        self.image_show.setPixmap(QtGui.QPixmap(self.im_path))
