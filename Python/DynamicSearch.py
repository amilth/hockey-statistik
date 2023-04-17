from PySide6.QtWidgets import QWidget, QComboBox
from PySide6.QtCore import Slot
from ui.widget_DynamicSearch_ui import Ui_DynamicSearch
import Functions
import Settings


class DynamicSearch(QWidget, Ui_DynamicSearch):
    def __init__(self, parent):
        super(DynamicSearch, self).__init__(parent)
        self.setupUi(self)

        self.schema = "hockey"
        self.agg_types = Functions.get_list_all_pandas_compute_functions()

        self.tables = Functions.get_db_tables(self.schema, Settings.dbconn)
        self.replace_values_in_comboBox(self.cb_Tables, self.tables)
        self.cb_Tables.activated.connect(self.get_value_from_cb_Tables)

        self.pb_UseSelection.clicked.connect(self.pb_use_selection)

    def add_values_to_comboBox(self, comboBoxName: QComboBox, values):
        comboBoxName.addItems(values)

    def empty_comboBox(self, comboBoxName: QComboBox):
        comboBoxName.clear()

    def replace_values_in_comboBox(self, comboBoxName: QComboBox, values):
        self.empty_comboBox(comboBoxName)
        comboBoxName.addItems(values)

    def get_value_from_cb_Tables(self):
        self.table = None
        self.table = self.cb_Tables.currentText()
        self.columns = Functions.get_table_columns(
            self.schema, self.table, Settings.dbconn)
        self.replace_values_in_comboBox(self.cb_GroupByColumn, self.columns)
        self.replace_values_in_comboBox(self.cb_AggregateColumn, self.columns)
        self.replace_values_in_comboBox(self.cb_AggregateType, self.agg_types)

    @Slot()
    def pb_use_selection(self):
        print("Using Selected properties")
        selection = (f"select {self.cb_GroupByColumn.currentText()}"+"\n"
                     f"     , {self.cb_AggregateType.currentText()}({self.cb_AggregateColumn.currentText()})"+"\n"
                     f"from {self.cb_Tables.currentText()}"+"\n"
                     f"group by {self.cb_GroupByColumn.currentText()}")

        self.tl_resultText.setText(selection)
