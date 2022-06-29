from mysql.connector import connect, Error
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from PyQt6 import uic
import sys


#Hämta in ui gränssnittet från designverktyget.
class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Python\\main_ui_window.ui", self)

        self.dBConn = None

        #Window.ButtonName.Event.RunThis
        self.pushButtonConnectToDB.clicked.connect(self.ConnectToDB)
        self.pushButtonDisconnectFromDB.clicked.connect(self.DisconnectFromDB)
        self.pushButtonTopTen.clicked.connect(lambda: self.GetTop10Players(10))
        #ToDo: lägg till kod för knapp top 10 teams.
        #ToDo: lägg till kod för knapp top 10 events.
        
    def ConnectToDB(self):
        try:
            self.dBConn = connect(
                host="185.157.160.111",
                port="33306",
                user="my_db_admin",
                password="mysql",
                database="hockey"
            )

            if self.dBConn:
                QMessageBox.information(
                    None,
                    "App Name - Success!",
                    "Connected to {} at {}".format(
                        self.dBConn._database, 
                        self.dBConn._host
                        ),
                )

        except Error as err:
            QMessageBox.critical(
                None,
                "App Name - Error!",
                "Database Error: {}".format(err._full_msg),
            )
            sys.exit(1)
        

    def DisconnectFromDB(self):
        if not self.dBConn:
            print("Nothing to disconnect.")
            return
        self.dBConn.close()
        self.dBConn = None
        print('Disconnected from MySQL database.')


    def GetTop10Players(self, limit):
        if not self.dBConn:
            print("No connection found.")
            return
        
        cursor = self.dBConn.cursor()
        query = """SELECT p.PlayerName as 'Player Name'
                        , p.Country as 'Country'
                        , count(g.GoalScorerId) as 'Goals'
                    FROM hockey.event_goal as g
                    join hockey.player as p on p.PlayerId = g.GoalScorerId
                    group by g.GoalScorerId
                    order by count(g.GoalScorerId) desc
                    limit %s;"""
        cursor.execute(query, (limit,))

        self.tableWidgetTopTen.setColumnCount(len(cursor.column_names))
        self.tableWidgetTopTen.setRowCount(limit)
        self.tableWidgetTopTen.setHorizontalHeaderLabels(cursor.column_names)
        
        self.AddDataToTable(cursor.fetchall())

        
    def AddDataToTable(self, data):
        for rowNum, rowData in enumerate(data):
            for colNum, colData in enumerate(rowData):
                self.tableWidgetTopTen.setItem(rowNum, colNum, QTableWidgetItem(str(colData)))
        

#Initiera UI-fönstret från designverktyget.
app = QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec())