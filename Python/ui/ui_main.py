# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1255, 884)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(200, 16777215))
        self.frame.setStyleSheet(u"QPushButton {\n"
"	min-height: 50px\n"
"}\n"
"QFrame {\n"
"	min-width: 200px\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pb_LoadWidget1 = QPushButton(self.frame)
        self.pb_LoadWidget1.setObjectName(u"pb_LoadWidget1")

        self.verticalLayout_2.addWidget(self.pb_LoadWidget1)

        self.pushButton_7 = QPushButton(self.frame)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_2.addWidget(self.pushButton_7)

        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_2.addWidget(self.pushButton_6)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_2.addWidget(self.pushButton_5)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.pb_ConnectToDb = QPushButton(self.frame)
        self.pb_ConnectToDb.setObjectName(u"pb_ConnectToDb")

        self.verticalLayout_2.addWidget(self.pb_ConnectToDb)


        self.horizontalLayout.addWidget(self.frame)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_7 = QHBoxLayout(self.page)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tl_Tables = QLabel(self.page)
        self.tl_Tables.setObjectName(u"tl_Tables")

        self.horizontalLayout_2.addWidget(self.tl_Tables)

        self.cb_Tables = QComboBox(self.page)
        self.cb_Tables.addItem("")
        self.cb_Tables.setObjectName(u"cb_Tables")
        self.cb_Tables.setMaxVisibleItems(20)
        self.cb_Tables.setFrame(True)

        self.horizontalLayout_2.addWidget(self.cb_Tables)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tl_GroupByColumn = QLabel(self.page)
        self.tl_GroupByColumn.setObjectName(u"tl_GroupByColumn")

        self.horizontalLayout_3.addWidget(self.tl_GroupByColumn)

        self.cb_GroupByColumn = QComboBox(self.page)
        self.cb_GroupByColumn.setObjectName(u"cb_GroupByColumn")

        self.horizontalLayout_3.addWidget(self.cb_GroupByColumn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tl_AggregateColumn = QLabel(self.page)
        self.tl_AggregateColumn.setObjectName(u"tl_AggregateColumn")

        self.horizontalLayout_4.addWidget(self.tl_AggregateColumn)

        self.cb_AggregateColumn = QComboBox(self.page)
        self.cb_AggregateColumn.setObjectName(u"cb_AggregateColumn")

        self.horizontalLayout_4.addWidget(self.cb_AggregateColumn)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tl_AggregateType = QLabel(self.page)
        self.tl_AggregateType.setObjectName(u"tl_AggregateType")

        self.horizontalLayout_5.addWidget(self.tl_AggregateType)

        self.cb_AggregateType = QComboBox(self.page)
        self.cb_AggregateType.setObjectName(u"cb_AggregateType")

        self.horizontalLayout_5.addWidget(self.cb_AggregateType)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pb_UseSelection = QPushButton(self.page)
        self.pb_UseSelection.setObjectName(u"pb_UseSelection")

        self.verticalLayout.addWidget(self.pb_UseSelection)


        self.horizontalLayout_7.addLayout(self.verticalLayout)

        self.tl_resultText = QLabel(self.page)
        self.tl_resultText.setObjectName(u"tl_resultText")
        sizePolicy.setHeightForWidth(self.tl_resultText.sizePolicy().hasHeightForWidth())
        self.tl_resultText.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.tl_resultText)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1255, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.tl_Tables.setBuddy(self.cb_Tables)
        self.tl_GroupByColumn.setBuddy(self.cb_GroupByColumn)
        self.tl_AggregateColumn.setBuddy(self.cb_AggregateColumn)
        self.tl_AggregateType.setBuddy(self.cb_AggregateType)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.pb_LoadWidget1, self.pushButton_7)
        QWidget.setTabOrder(self.pushButton_7, self.pushButton_6)
        QWidget.setTabOrder(self.pushButton_6, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.pushButton_5)
        QWidget.setTabOrder(self.pushButton_5, self.pb_ConnectToDb)
        QWidget.setTabOrder(self.pb_ConnectToDb, self.cb_Tables)
        QWidget.setTabOrder(self.cb_Tables, self.cb_GroupByColumn)
        QWidget.setTabOrder(self.cb_GroupByColumn, self.cb_AggregateColumn)
        QWidget.setTabOrder(self.cb_AggregateColumn, self.cb_AggregateType)
        QWidget.setTabOrder(self.cb_AggregateType, self.pb_UseSelection)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pb_LoadWidget1.setText(QCoreApplication.translate("MainWindow", u"Load Widget 1", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pb_ConnectToDb.setText(QCoreApplication.translate("MainWindow", u"Connect to DB", None))
        self.tl_Tables.setText(QCoreApplication.translate("MainWindow", u"Table", None))
        self.cb_Tables.setItemText(0, "")

        self.tl_GroupByColumn.setText(QCoreApplication.translate("MainWindow", u"Group by column", None))
        self.tl_AggregateColumn.setText(QCoreApplication.translate("MainWindow", u"Aggregate column", None))
        self.tl_AggregateType.setText(QCoreApplication.translate("MainWindow", u"Aggregate type", None))
        self.pb_UseSelection.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.tl_resultText.setText(QCoreApplication.translate("MainWindow", u"TextLabel2", None))
    # retranslateUi

