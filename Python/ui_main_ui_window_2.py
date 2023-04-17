# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui_window_2.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1129, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButtonAddDataToDatabase = QPushButton(self.centralwidget)
        self.pushButtonAddDataToDatabase.setObjectName(u"pushButtonAddDataToDatabase")
        self.pushButtonAddDataToDatabase.setGeometry(QRect(90, 152, 232, 41))
        self.pushButtonAddDataToDatabase.setMaximumSize(QSize(250, 16777215))
        self.pushButtonAddDataToDatabase.setStyleSheet(u"QPushButton")
        self.pushButtonSearchDatabase = QPushButton(self.centralwidget)
        self.pushButtonSearchDatabase.setObjectName(u"pushButtonSearchDatabase")
        self.pushButtonSearchDatabase.setGeometry(QRect(450, 152, 232, 41))
        self.pushButtonSearchDatabase.setMaximumSize(QSize(250, 16777215))
        self.pushButtonSearchDatabase.setStyleSheet(u"QPushButton")
        self.pushButtonConnectToDB = QPushButton(self.centralwidget)
        self.pushButtonConnectToDB.setObjectName(u"pushButtonConnectToDB")
        self.pushButtonConnectToDB.setGeometry(QRect(90, 80, 232, 41))
        self.pushButtonConnectToDB.setMaximumSize(QSize(250, 16777215))
        self.pushButtonDisconnectFromDB = QPushButton(self.centralwidget)
        self.pushButtonDisconnectFromDB.setObjectName(u"pushButtonDisconnectFromDB")
        self.pushButtonDisconnectFromDB.setGeometry(QRect(450, 80, 232, 41))
        self.pushButtonDisconnectFromDB.setMaximumSize(QSize(250, 16777215))
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(400, 340, 42, 22))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1129, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButtonAddDataToDatabase.setText(QCoreApplication.translate("MainWindow", u"Add data to database", None))
        self.pushButtonSearchDatabase.setText(QCoreApplication.translate("MainWindow", u"Search database", None))
        self.pushButtonConnectToDB.setText(QCoreApplication.translate("MainWindow", u"ConnectToDB", None))
        self.pushButtonDisconnectFromDB.setText(QCoreApplication.translate("MainWindow", u"DisconnectFromDB", None))
    # retranslateUi

