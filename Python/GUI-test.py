import sys
# import pandas as pd
# import matplotlib.pyplot as plt
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox
# from PySide6.QtWidgets import QDialog

from functions import *
from ui.ui_main import Ui_MainWindow
# from ui.ui_dialog_ConnectToDatabase import Ui_Dialog

dbconn = None


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # self.dbconn = ConnectToMySQLDBviaSQLAlchemy()
        self.pb_ConnectToDb.clicked.connect(self.connect_to_dasabase)
        self.pb_LoadWidget1.clicked.connect(self.load_widget_1)

    def add_values_to_comboBox(self, comboBoxName: QtWidgets.QComboBox, values):
        comboBoxName.addItems(values)

    def empty_comboBox(self, comboBoxName: QtWidgets.QComboBox):
        comboBoxName.clear()

    def replace_values_in_comboBox(self, comboBoxName: QtWidgets.QComboBox, values):
        self.empty_comboBox(comboBoxName)
        comboBoxName.addItems(values)

    def get_value_from_cb_Tables(self):
        self.table = None
        self.table = self.cb_Tables.currentText()
        self.columns = get_table_columns(self.schema, self.table, dbconn)
        self.replace_values_in_comboBox(self.cb_GroupByColumn, self.columns)
        self.replace_values_in_comboBox(self.cb_AggregateColumn, self.columns)
        self.replace_values_in_comboBox(self.cb_AggregateType, self.agg_types)

    def pb_use_selection(self):
        selection = (f"select {self.cb_GroupByColumn.currentText()}"+"\n"
                     f"     , {self.cb_AggregateType.currentText()}({self.cb_AggregateColumn.currentText()})"+"\n"
                     f"from {self.cb_Tables.currentText()}"+"\n"
                     f"group by {self.cb_GroupByColumn.currentText()}")

        self.tl_resultText.setText(selection)

    def connect_to_dasabase(self, s):
        global dbconn
        dbconn = ConnectToMySQLDBviaSQLAlchemy()

    def load_widget_1(self):
        if dbconn is None:
            # print("Connect to a database first")
            self.show_warning("Connect to a database first")
            return
        self.schema = "hockey"
        self.agg_types = get_list_all_pandas_compute_functions()

        self.tables = get_db_tables(self.schema, dbconn)
        self.replace_values_in_comboBox(self.cb_Tables, self.tables)
        self.cb_Tables.activated.connect(self.get_value_from_cb_Tables)

        self.pb_UseSelection.clicked.connect(self.pb_use_selection)

    def show_warning(self, warning_message):
        msg_box = QMessageBox()
        msg_box.setText(warning_message)
        msg_box.setIcon(QMessageBox.Warning)
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
