import sqlalchemy as db
import pandas as pd
import re

from PySide6.QtWidgets import QDialog
from ui.dialog_ConnectToDatabase_ui import Ui_Dialog


def ConnectToMySQLDBviaSQLAlchemy():
    dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(dialog)
    state = dialog.exec()
    if state == 1:
        driver = ui.cb_driver.currentText()
        username = ui.le_username.text()
        password = ui.le_password.text()
        host = ui.le_host.text()
        port = ui.le_port.text()
        dataBase = ui.le_database.text()

        connString = f"{driver}://{username}:{password}@{host}:{port}/{dataBase}"
        engine = db.create_engine(connString)
        connection = engine.connect()
        return connection

    if state == 0:
        return None


def convert_height_str_to_m(height_str):
    FEET_TO_M = 0.3048
    pattern = re.compile(r"""(\d+)' *(\d+)(?:"|'')?""")
    feet, inches = map(float, re.match(pattern, height_str).groups())
    return FEET_TO_M * (feet + inches/12)


def convert_height_str_to_cm(height_str):
    return convert_height_str_to_m(height_str) * 100.0


def get_db_tables(dataBase, connection):
    query = f'''select TABLE_NAME 
                from INFORMATION_SCHEMA.TABLES 
                where TABLE_SCHEMA = '{dataBase}' 
                order by TABLE_NAME'''
    df = pd.read_sql(db.text(query), connection)
    tables = df.squeeze()
    return tables


def get_table_columns(dataBase, table, connection):
    query = f'''select COLUMN_NAME
                from INFORMATION_SCHEMA.COLUMNS
                where TABLE_SCHEMA = '{dataBase}'
	                and TABLE_NAME = '{table}'
                order by COLUMN_NAME'''
    df = pd.read_sql(db.text(query), connection)
    columns = df.squeeze()
    return columns


def get_list_all_pandas_compute_functions():
    agg_list = ['count', 'first', 'last', 'max', 'mean', 'median',
                'min', 'ohlc', 'prod', 'size', 'sem', 'std', 'sum', 'var']
    agg_list.sort()
    return agg_list
