# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_KingComic.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(518, 618)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tl_pixm_KingComic = QLabel(Form)
        self.tl_pixm_KingComic.setObjectName(u"tl_pixm_KingComic")
        self.tl_pixm_KingComic.setPixmap(QPixmap(u"../../../../../../../../Bilder/King Comics/43873_tech-support.jpg"))
        self.tl_pixm_KingComic.setScaledContents(False)
        self.tl_pixm_KingComic.setAlignment(Qt.AlignCenter)
        self.tl_pixm_KingComic.setOpenExternalLinks(True)

        self.horizontalLayout.addWidget(self.tl_pixm_KingComic)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.tl_pixm_KingComic.setText("")
    # retranslateUi

