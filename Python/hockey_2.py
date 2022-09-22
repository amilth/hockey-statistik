from mysql.connector import connect, Error
from PyQt5 import uic, QtChart
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
import sys
from hockey_main import SEARCH

#Hämta in ui gränssnittet från designverktyget.
class UI(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("Python\\main_ui_window_2.ui", self)

        self.dBConn = None

        #Window.ButtonName.Event.RunThis
        self.pushButtonConnectToDB.clicked.connect(self.ConnectToDB)
        self.pushButtonDisconnectFromDB.clicked.connect(self.DisconnectFromDB)
        self.pushButtonSearchDatabase.clicked.connect(lambda: self.SearchDatabase(10))
        # self.pushButtonAddDataToDatabase.clicked.connect(lambda: self.AddDataToDatabase)

        
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
            # print("Nothing to disconnect.")
            return
        database = self.dBConn._database
        host = self.dBConn._host
        self.dBConn.close()
        self.dBConn = None
        if not self.dBConn:
            QMessageBox.information(
                None,
                "App Name - Success!",
                "Disconnected from {} at {}".format(
                    database, 
                    host
                    ),
            )
            # print('Disconnected from MySQL database.')
            # sys.exit(app.exec())


    def SearchDatabase(self, limit):
        if not self.dBConn:
            print("No connection found.")
            return
        uic.loadUi("Python\\main_ui_window.ui", self)
        SEARCH.skycake()
        limit = 10

        self.pushButtonTopTenPlayers.clicked.connect(lambda: SEARCH.GetTop10Players(self, limit))
        self.pushButtonTopTenTeams.clicked.connect(lambda: SEARCH.GetTop10Teams(self, limit))
        self.pushButtonTopTenSalaries.clicked.connect(lambda: SEARCH.GetTop10Salaries(self, limit))
        
        #from testing import GetTop10Players
        cursor = self.dBConn.cursor()

        
#Initiera UI-fönstret från designverktyget.
app = QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec())