#!/usr/bin/env python
# coding: utf-8
# reference : https://github.com/andriyantohalim/PySide2_Tutorial

import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.move(300, 150)
        self.setWindowTitle('GridLayout')
        self.show()

    def initUI(self):
        names = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        grid = QGridLayout()

        j = 0
        pos = [(0, 0), (0, 1), (0, 2),
               (1, 0), (1, 1), (1, 2),
               (2, 0), (2, 1), (2, 2)]

        for i in names:
            button = QPushButton(i)
            grid.addWidget(button, pos[j][0], pos[j][1])
            j = j + 1

        self.setLayout(grid)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
