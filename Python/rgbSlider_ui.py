# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rgbSlider.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QSlider, QSpinBox, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(340, 294)
        self.gridLayout_4 = QGridLayout(Form)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.labelRed = QLabel(Form)
        self.labelRed.setObjectName(u"labelRed")

        self.gridLayout.addWidget(self.labelRed, 0, 0, 1, 1)

        self.spinBoxRed = QSpinBox(Form)
        self.spinBoxRed.setObjectName(u"spinBoxRed")
        self.spinBoxRed.setMaximum(255)

        self.gridLayout.addWidget(self.spinBoxRed, 1, 0, 1, 1)

        self.verticalSliderRed = QSlider(Form)
        self.verticalSliderRed.setObjectName(u"verticalSliderRed")
        self.verticalSliderRed.setMaximum(255)
        self.verticalSliderRed.setOrientation(Qt.Vertical)

        self.gridLayout.addWidget(self.verticalSliderRed, 2, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.labelGreen = QLabel(Form)
        self.labelGreen.setObjectName(u"labelGreen")

        self.gridLayout_2.addWidget(self.labelGreen, 0, 0, 1, 1)

        self.spinBoxGreen = QSpinBox(Form)
        self.spinBoxGreen.setObjectName(u"spinBoxGreen")
        self.spinBoxGreen.setMaximum(255)

        self.gridLayout_2.addWidget(self.spinBoxGreen, 1, 0, 1, 1)

        self.verticalSliderGreen = QSlider(Form)
        self.verticalSliderGreen.setObjectName(u"verticalSliderGreen")
        self.verticalSliderGreen.setMaximum(255)
        self.verticalSliderGreen.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSliderGreen, 2, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.labelBlue = QLabel(Form)
        self.labelBlue.setObjectName(u"labelBlue")

        self.gridLayout_3.addWidget(self.labelBlue, 0, 0, 1, 1)

        self.spinBoxBlue = QSpinBox(Form)
        self.spinBoxBlue.setObjectName(u"spinBoxBlue")
        self.spinBoxBlue.setMaximum(255)

        self.gridLayout_3.addWidget(self.spinBoxBlue, 1, 0, 1, 1)

        self.verticalSliderBlue = QSlider(Form)
        self.verticalSliderBlue.setObjectName(u"verticalSliderBlue")
        self.verticalSliderBlue.setMaximum(255)
        self.verticalSliderBlue.setOrientation(Qt.Vertical)

        self.gridLayout_3.addWidget(self.verticalSliderBlue, 2, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 2, 1, 1)


        self.retranslateUi(Form)
        self.spinBoxRed.valueChanged.connect(self.verticalSliderRed.setValue)
        self.verticalSliderRed.valueChanged.connect(self.spinBoxRed.setValue)
        self.spinBoxGreen.valueChanged.connect(self.verticalSliderGreen.setValue)
        self.verticalSliderGreen.valueChanged.connect(self.spinBoxGreen.setValue)
        self.spinBoxBlue.valueChanged.connect(self.verticalSliderBlue.setValue)
        self.verticalSliderBlue.valueChanged.connect(self.spinBoxBlue.setValue)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.labelRed.setText(QCoreApplication.translate("Form", u"RED", None))
        self.labelGreen.setText(QCoreApplication.translate("Form", u"GREEN", None))
        self.labelBlue.setText(QCoreApplication.translate("Form", u"BLUE", None))
    # retranslateUi

