#!/usr/bin/env python
# coding: utf-8
# reference : https://github.com/andriyantohalim/PySide2_Tutorial

import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setGeometry(300, 300, 400, 100)
        self.setWindowTitle('BoxLayout')
        self.show()

    def initUI(self):
        btn_ok = QPushButton('了解')
        btn_cancel = QPushButton('キャンセル')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn_ok)
        hbox.addWidget(btn_cancel)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
