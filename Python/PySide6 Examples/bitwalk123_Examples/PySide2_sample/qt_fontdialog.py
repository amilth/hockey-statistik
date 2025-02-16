#!/usr/bin/env python
# coding: utf-8
# reference : https://github.com/andriyantohalim/PySide2_Tutorial

import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QFontDialog, QLabel, QVBoxLayout, QSizePolicy


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setGeometry(300, 300, 250, 200)
        self.setWindowTitle('Font dialog')
        self.show()

    def initUI(self):
        vbox = QVBoxLayout()

        btn = QPushButton('フォント選択', self)
        btn.setSizePolicy(QSizePolicy.Fixed,
                          QSizePolicy.Fixed)

        btn.move(20, 20)

        vbox.addWidget(btn)

        btn.clicked.connect(self.showDialog)

        self.lbl = QLabel('フォントサンプル : abcdef ABCDEF', self)
        self.lbl.move(100, 20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

    def showDialog(self):
        ok, font = QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
