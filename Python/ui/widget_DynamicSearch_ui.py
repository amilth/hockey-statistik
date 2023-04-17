# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_DynamicSearch.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_DynamicSearch(object):
    def setupUi(self, DynamicSearch):
        if not DynamicSearch.objectName():
            DynamicSearch.setObjectName(u"DynamicSearch")
        DynamicSearch.resize(667, 546)
        self.horizontalLayout = QHBoxLayout(DynamicSearch)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.layout_SelectionParameters = QVBoxLayout()
        self.layout_SelectionParameters.setObjectName(u"layout_SelectionParameters")
        self.vs_SelectionTop = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout_SelectionParameters.addItem(self.vs_SelectionTop)

        self.layout_Table = QHBoxLayout()
        self.layout_Table.setObjectName(u"layout_Table")
        self.tl_Table = QLabel(DynamicSearch)
        self.tl_Table.setObjectName(u"tl_Table")

        self.layout_Table.addWidget(self.tl_Table)

        self.cb_Tables = QComboBox(DynamicSearch)
        self.cb_Tables.setObjectName(u"cb_Tables")

        self.layout_Table.addWidget(self.cb_Tables)


        self.layout_SelectionParameters.addLayout(self.layout_Table)

        self.layout_GroupByColumn = QHBoxLayout()
        self.layout_GroupByColumn.setObjectName(u"layout_GroupByColumn")
        self.tl_GroupByColumn = QLabel(DynamicSearch)
        self.tl_GroupByColumn.setObjectName(u"tl_GroupByColumn")

        self.layout_GroupByColumn.addWidget(self.tl_GroupByColumn)

        self.cb_GroupByColumn = QComboBox(DynamicSearch)
        self.cb_GroupByColumn.setObjectName(u"cb_GroupByColumn")

        self.layout_GroupByColumn.addWidget(self.cb_GroupByColumn)


        self.layout_SelectionParameters.addLayout(self.layout_GroupByColumn)

        self.layout_AggregateColumn = QHBoxLayout()
        self.layout_AggregateColumn.setObjectName(u"layout_AggregateColumn")
        self.tl_AggregateColumn = QLabel(DynamicSearch)
        self.tl_AggregateColumn.setObjectName(u"tl_AggregateColumn")

        self.layout_AggregateColumn.addWidget(self.tl_AggregateColumn)

        self.cb_AggregateColumn = QComboBox(DynamicSearch)
        self.cb_AggregateColumn.setObjectName(u"cb_AggregateColumn")

        self.layout_AggregateColumn.addWidget(self.cb_AggregateColumn)


        self.layout_SelectionParameters.addLayout(self.layout_AggregateColumn)

        self.layout_AggregateType = QHBoxLayout()
        self.layout_AggregateType.setObjectName(u"layout_AggregateType")
        self.tl_AggregateType = QLabel(DynamicSearch)
        self.tl_AggregateType.setObjectName(u"tl_AggregateType")

        self.layout_AggregateType.addWidget(self.tl_AggregateType)

        self.cb_AggregateType = QComboBox(DynamicSearch)
        self.cb_AggregateType.setObjectName(u"cb_AggregateType")

        self.layout_AggregateType.addWidget(self.cb_AggregateType)


        self.layout_SelectionParameters.addLayout(self.layout_AggregateType)

        self.vs_SelectionBottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.layout_SelectionParameters.addItem(self.vs_SelectionBottom)

        self.pb_UseSelection = QPushButton(DynamicSearch)
        self.pb_UseSelection.setObjectName(u"pb_UseSelection")

        self.layout_SelectionParameters.addWidget(self.pb_UseSelection)


        self.horizontalLayout.addLayout(self.layout_SelectionParameters)

        self.tl_RightText = QLabel(DynamicSearch)
        self.tl_RightText.setObjectName(u"tl_RightText")

        self.horizontalLayout.addWidget(self.tl_RightText)


        self.retranslateUi(DynamicSearch)

        QMetaObject.connectSlotsByName(DynamicSearch)
    # setupUi

    def retranslateUi(self, DynamicSearch):
        DynamicSearch.setWindowTitle(QCoreApplication.translate("DynamicSearch", u"Form", None))
        self.tl_Table.setText(QCoreApplication.translate("DynamicSearch", u"Table", None))
        self.tl_GroupByColumn.setText(QCoreApplication.translate("DynamicSearch", u"Group by column", None))
        self.tl_AggregateColumn.setText(QCoreApplication.translate("DynamicSearch", u"Aggregate column", None))
        self.tl_AggregateType.setText(QCoreApplication.translate("DynamicSearch", u"Aggregate type", None))
        self.pb_UseSelection.setText(QCoreApplication.translate("DynamicSearch", u"PushButton", None))
        self.tl_RightText.setText(QCoreApplication.translate("DynamicSearch", u"Right Text", None))
    # retranslateUi

