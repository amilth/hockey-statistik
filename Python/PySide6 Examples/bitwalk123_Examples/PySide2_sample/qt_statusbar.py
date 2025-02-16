#!/usr/bin/env python
# coding: utf-8
# reference : https://github.com/andriyantohalim/PySide2_Tutorial

import sys
from PySide6.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setGeometry(300, 300, 200, 150)
        self.setWindowTitle("Status Bar")
        self.show()

    def initUI(self):
        self.statusBar().showMessage('準備完了')


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
