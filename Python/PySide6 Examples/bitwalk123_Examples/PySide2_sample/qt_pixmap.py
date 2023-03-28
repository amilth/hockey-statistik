#!/usr/bin/env python
# coding: utf-8

import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import (
    QImage,
    QPixmap,
)
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLayout,
    QVBoxLayout,
    QWidget,
)


class Example(QWidget):
    length_max = 500.0
    file_name = 'hockey-statistik\Python\PySide2_sample\sample_picture.jpg'

    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle('QPixmap')
        self.setWindowFlags(Qt.WindowMinimizeButtonHint |
                            Qt.WindowCloseButtonHint)
        self.show()

    def initUI(self):
        image = QImage(self.file_name)
        if image.width() > image.height():
            pixmap = QPixmap(image.scaledToWidth(self.length_max))
        else:
            pixmap = QPixmap(image.scaledToHeight(self.length_max))

        label = QLabel(self)
        label.setPixmap(pixmap)

        vbox = QVBoxLayout(self)
        vbox.addWidget(label)
        vbox.setSizeConstraint(QLayout.SetFixedSize)
        self.setLayout(vbox)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
