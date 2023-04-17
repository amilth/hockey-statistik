import sys
import Settings
import Functions
from PySide6 import QtWidgets
from PySide6 import QtCore
from ui.main_ui import Ui_MainWindow
from ThreeWaySlider import ThreeWaySlider
from DynamicSearch import DynamicSearch

# import pandas as pd
# import matplotlib.pyplot as plt

Settings.init()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # self.dbconn = ConnectToMySQLDBviaSQLAlchemy()
        self.pb_ConnectToDb.clicked.connect(self.connect_to_dasabase)
        self.pb_LoadWidget1.clicked.connect(self.load_widget_1)
        self.pb_LoadWidget2.clicked.connect(self.load_widget_2)

    def connect_to_dasabase(self):
        Settings.dbconn = Functions.ConnectToMySQLDBviaSQLAlchemy()

    def load_widget_1(self):
        if Settings.dbconn is None:
            self.show_warning("Connect to a database first")
            return
        self.load_widget_multi(self.layout_RightWidget, DynamicSearch(self))

    def load_widget_2(self):
        if Settings.dbconn is None:
            self.show_warning("Connect to a database first")
            return
        self.load_widget_multi(self.layout_RightWidget, ThreeWaySlider())

    def load_widget_multi(self, layout, ui_class):
        widget = QtWidgets.QWidget()
        w_ui = ui_class
        w_ui.setupUi(widget)
        self.deleteItemsOfLayout(layout)
        layout.addWidget(widget)

    def deleteItemsOfLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)
                else:
                    self.deleteItemsOfLayout(item.layout())

    def show_warning(self, warning_message):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setText(warning_message)
        msg_box.setIcon(QtWidgets.QMessageBox.Warning)
        msg_box.setWindowTitle("Warning!")
        msg_box.exec()


# dbconn = ConnectToMySQLDBviaSQLAlchemy()
# table = 'player'
# df = pd.read_sql_table(table, dbconn)
# df['Height_cm'] = df['Height'].apply(convert_height_str_to_cm).round(2)
# df.groupby('Height_cm')['PlayerId'] \
#     .size() \
#     .sort_index(ascending=True) \
#     .plot(kind='bar',
#           figsize=(10, 5),
#           title='Heights in NHL')
# plt.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
