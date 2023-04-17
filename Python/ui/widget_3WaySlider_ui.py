# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'widget_3WaySlider.ui'
##
# Created by: Qt User Interface Compiler version 6.3.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDial, QHBoxLayout, QSizePolicy,
                               QSlider, QSpinBox, QVBoxLayout, QWidget)


class Ui_ThreeWaySlider(object):
    def setupUi(self, ThreeWaySlider):
        if not ThreeWaySlider.objectName():
            ThreeWaySlider.setObjectName(u"ThreeWaySlider")
        ThreeWaySlider.resize(577, 464)
        self.layout_ThreeWaySlider = QHBoxLayout(ThreeWaySlider)
        self.layout_ThreeWaySlider.setObjectName(u"layout_ThreeWaySlider")
        self.verticalLayout_left = QVBoxLayout()
        self.verticalLayout_left.setObjectName(u"verticalLayout_left")
        self.horizontalLayout_slider_left = QHBoxLayout()
        self.horizontalLayout_slider_left.setObjectName(
            u"horizontalLayout_slider_left")
        self.verticalSlider_left = QSlider(ThreeWaySlider)
        self.verticalSlider_left.setObjectName(u"verticalSlider_left")
        self.verticalSlider_left.setOrientation(Qt.Vertical)

        self.horizontalLayout_slider_left.addWidget(self.verticalSlider_left)

        self.verticalLayout_left.addLayout(self.horizontalLayout_slider_left)

        self.dial_left = QDial(ThreeWaySlider)
        self.dial_left.setObjectName(u"dial_left")

        self.verticalLayout_left.addWidget(self.dial_left)

        self.spinBox_left = QSpinBox(ThreeWaySlider)
        self.spinBox_left.setObjectName(u"spinBox_left")

        self.verticalLayout_left.addWidget(self.spinBox_left)

        self.layout_ThreeWaySlider.addLayout(self.verticalLayout_left)

        self.verticalLayout_middle = QVBoxLayout()
        self.verticalLayout_middle.setObjectName(u"verticalLayout_middle")
        self.horizontalLayout_slider_middle = QHBoxLayout()
        self.horizontalLayout_slider_middle.setObjectName(
            u"horizontalLayout_slider_middle")
        self.verticalSlider_middle = QSlider(ThreeWaySlider)
        self.verticalSlider_middle.setObjectName(u"verticalSlider_middle")
        self.verticalSlider_middle.setOrientation(Qt.Vertical)

        self.horizontalLayout_slider_middle.addWidget(
            self.verticalSlider_middle)

        self.verticalLayout_middle.addLayout(
            self.horizontalLayout_slider_middle)

        self.dial_middle = QDial(ThreeWaySlider)
        self.dial_middle.setObjectName(u"dial_middle")

        self.verticalLayout_middle.addWidget(self.dial_middle)

        self.spinBox_middle = QSpinBox(ThreeWaySlider)
        self.spinBox_middle.setObjectName(u"spinBox_middle")

        self.verticalLayout_middle.addWidget(self.spinBox_middle)

        self.layout_ThreeWaySlider.addLayout(self.verticalLayout_middle)

        self.verticalLayout_right = QVBoxLayout()
        self.verticalLayout_right.setObjectName(u"verticalLayout_right")
        self.horizontalLayout_slider_right = QHBoxLayout()
        self.horizontalLayout_slider_right.setObjectName(
            u"horizontalLayout_slider_right")
        self.verticalSlider_right = QSlider(ThreeWaySlider)
        self.verticalSlider_right.setObjectName(u"verticalSlider_right")
        self.verticalSlider_right.setOrientation(Qt.Vertical)

        self.horizontalLayout_slider_right.addWidget(self.verticalSlider_right)

        self.verticalLayout_right.addLayout(self.horizontalLayout_slider_right)

        self.dial_right = QDial(ThreeWaySlider)
        self.dial_right.setObjectName(u"dial_right")

        self.verticalLayout_right.addWidget(self.dial_right)

        self.spinBox_right = QSpinBox(ThreeWaySlider)
        self.spinBox_right.setObjectName(u"spinBox_right")

        self.verticalLayout_right.addWidget(self.spinBox_right)

        self.layout_ThreeWaySlider.addLayout(self.verticalLayout_right)

        self.retranslateUi(ThreeWaySlider)
        self.verticalSlider_left.sliderMoved.connect(self.dial_left.setValue)
        self.verticalSlider_left.sliderMoved.connect(
            self.spinBox_left.setValue)
        self.verticalSlider_middle.sliderMoved.connect(
            self.dial_middle.setValue)
        self.verticalSlider_middle.sliderMoved.connect(
            self.spinBox_middle.setValue)
        self.verticalSlider_right.sliderMoved.connect(self.dial_right.setValue)
        self.verticalSlider_right.sliderMoved.connect(
            self.spinBox_right.setValue)
        self.dial_left.sliderMoved.connect(self.verticalSlider_left.setValue)
        self.dial_left.sliderMoved.connect(self.spinBox_left.setValue)
        self.dial_middle.sliderMoved.connect(
            self.verticalSlider_middle.setValue)
        self.dial_middle.sliderMoved.connect(self.spinBox_middle.setValue)
        self.dial_right.sliderMoved.connect(self.verticalSlider_right.setValue)
        self.dial_right.sliderMoved.connect(self.spinBox_right.setValue)
        self.spinBox_left.valueChanged.connect(self.dial_left.setValue)
        self.spinBox_left.valueChanged.connect(
            self.verticalSlider_left.setValue)
        self.spinBox_middle.valueChanged.connect(self.dial_middle.setValue)
        self.spinBox_middle.valueChanged.connect(
            self.verticalSlider_middle.setValue)
        self.spinBox_right.valueChanged.connect(
            self.verticalSlider_right.setValue)
        self.spinBox_right.valueChanged.connect(self.dial_right.setValue)

        QMetaObject.connectSlotsByName(ThreeWaySlider)
    # setupUi

    def retranslateUi(self, ThreeWaySlider):
        ThreeWaySlider.setWindowTitle(
            QCoreApplication.translate("ThreeWaySlider", u"Form", None))
    # retranslateUi
