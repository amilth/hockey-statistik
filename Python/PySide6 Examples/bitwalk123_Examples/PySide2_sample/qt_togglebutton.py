#!/usr/bin/env python
# coding: utf-8
# reference : https://github.com/andriyantohalim/PySide2_Tutorial

import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QFrame
from PySide6.QtGui import QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle("Toggle Button")
        self.show()

    def initUI(self):

        self.col = QColor(0, 0, 0)

        redb = QPushButton('赤', self)
        redb.setCheckable(True)
        redb.move(10, 10)

        redb.clicked[bool].connect(self.setColor)

        greenb = QPushButton('緑', self)
        greenb.setCheckable(True)
        greenb.move(10, 60)

        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('青', self)
        blueb.setCheckable(True)
        blueb.move(10, 110)

        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet(
            "QWidget { background-color: %s }" % self.col.name())

    def setColor(self, pressed):
        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == '赤':
            self.col.setRed(val)
        elif source.text() == '緑':
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet(
            "QFrame { background-color: %s }" % self.col.name())


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
