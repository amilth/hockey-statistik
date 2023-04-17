# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui_window.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1127, 405)
        font = QFont()
        font.setFamilies([u"Tw Cen MT"])
        font.setPointSize(24)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QPushButton {\n"
"	\n"
"	font: 75 16pt \"MS Shell Dlg 2\";\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_coll = QFrame(self.centralwidget)
        self.button_coll.setObjectName(u"button_coll")
        self.button_coll.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout = QVBoxLayout(self.button_coll)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.pushButtonTopTenTeams = QPushButton(self.button_coll)
        self.pushButtonTopTenTeams.setObjectName(u"pushButtonTopTenTeams")
        self.pushButtonTopTenTeams.setMaximumSize(QSize(250, 16777215))
        self.pushButtonTopTenTeams.setStyleSheet(u"QPushButton")

        self.verticalLayout.addWidget(self.pushButtonTopTenTeams)

        self.pushButtonTopTenPlayers = QPushButton(self.button_coll)
        self.pushButtonTopTenPlayers.setObjectName(u"pushButtonTopTenPlayers")
        self.pushButtonTopTenPlayers.setMaximumSize(QSize(250, 16777215))
        self.pushButtonTopTenPlayers.setStyleSheet(u"QPushbutton{\n"
"            border-radius: 25 px;\n"
"            background-color:rgb(85, 170, 255);\n"
"            color:rgb(85, 85, 255);\n"
"            }\n"
"\n"
"            QPushbutton:hover{\n"
"            background-color:rgb(50, 110, 255);\n"
"            color:rgb(255,255, 255);\n"
"            }\n"
"\n"
"            QPushbutton:pressed{\n"
"            background-color:rgb(100, 170, 255);\n"
"            }\n"
"          ")

        self.verticalLayout.addWidget(self.pushButtonTopTenPlayers)

        self.pushButtonTopTenSalaries = QPushButton(self.button_coll)
        self.pushButtonTopTenSalaries.setObjectName(u"pushButtonTopTenSalaries")
        self.pushButtonTopTenSalaries.setMaximumSize(QSize(250, 16777215))
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dlg 2"])
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setItalic(False)
        self.pushButtonTopTenSalaries.setFont(font1)

        self.verticalLayout.addWidget(self.pushButtonTopTenSalaries)


        self.horizontalLayout.addWidget(self.button_coll)

        self.tableWidgetTopTen = QTableWidget(self.centralwidget)
        if (self.tableWidgetTopTen.columnCount() < 2):
            self.tableWidgetTopTen.setColumnCount(2)
        if (self.tableWidgetTopTen.rowCount() < 10):
            self.tableWidgetTopTen.setRowCount(10)
        self.tableWidgetTopTen.setObjectName(u"tableWidgetTopTen")
        self.tableWidgetTopTen.setMinimumSize(QSize(300, 0))
        self.tableWidgetTopTen.setMaximumSize(QSize(300, 16777215))
        self.tableWidgetTopTen.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidgetTopTen.setRowCount(10)
        self.tableWidgetTopTen.setColumnCount(2)

        self.horizontalLayout.addWidget(self.tableWidgetTopTen)

        self.chart_area = QWidget(self.centralwidget)
        self.chart_area.setObjectName(u"chart_area")
        self.chart_area.setEnabled(True)
        self.chart_area.setMinimumSize(QSize(300, 0))
        self.chart_area.setLayoutDirection(Qt.LeftToRight)
        self.chart_area.setAutoFillBackground(False)
        self.chart_area.setStyleSheet(u"")
        self.chart_area_layout = QVBoxLayout(self.chart_area)
        self.chart_area_layout.setSpacing(0)
        self.chart_area_layout.setObjectName(u"chart_area_layout")
        self.chart_area_layout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.chart_area)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1127, 21))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButtonTopTenTeams.setText(QCoreApplication.translate("MainWindow", u"Get top 10 Teams", None))
        self.pushButtonTopTenPlayers.setText(QCoreApplication.translate("MainWindow", u"Get top 10 players", None))
        self.pushButtonTopTenSalaries.setText(QCoreApplication.translate("MainWindow", u"Get highest 10 salaries", None))
    # retranslateUi

