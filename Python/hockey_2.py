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
      
"""
    def addDataToTable(self, data):
         for rowNum, rowData in enumerate(data):
             for colNum, colData in enumerate(rowData):
                 self.tableWidgetTopTen.setItem(rowNum, colNum, QTableWidgetItem(str(colData)))
        
            
    def addChartPie(self, data, chart_title, layout):
        players = [x[0] for x in data]
        goals = [x[1] for x in data]

        series = QtChart.QPieSeries()
        for x in players:
             series.append(x, goals[players.index(x)])

        slice = series.slices()[0]
        slice.setExploded()
        slice.setLabelVisible()
        slice.setPen(QPen(Qt.darkGreen, 2))
        slice.setBrush(Qt.green)
        
        chart = QtChart.QChart()
        chart.addSeries(series)
        chart.setTitle(chart_title)
        chart.legend().setAlignment(Qt.AlignLeft)
        chart.setAnimationOptions(QtChart.QChart.SeriesAnimations)
        chart.setTheme(QtChart.QChart.ChartTheme.ChartThemeQt)

        chartview = QtChart.QChartView(chart)

        self.chart_area.setContentsMargins(0, 0, 0, 0)
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.addChartInLayout(chartview, layout)


    def addChartStackedBar(self, data, chart_title, layout):
         teams = [x[0] for x in data]
         goals = [x[1] for x in data]

         series = QtChart.QBarSeries()
         for x in teams:
             setattr(self, "set"+str(x), QtChart.QBarSet(str(x)))
             series.append(getattr(self, "set"+str(x)))
             getattr(self, "set"+str(x)).append(goals[teams.index(x)])

         chart = QtChart.QChart()
         chart.addSeries(series)
         chart.setTitle(chart_title)
         chart.setAnimationOptions(QtChart.QChart.SeriesAnimations)

         categories = ["Goals"]
         axis = QtChart.QBarCategoryAxis()
         axis.append(categories)
         chart.createDefaultAxes()
         chart.setAxisX(axis, series)
         chart.legend().setAlignment(Qt.AlignLeft)

         chartview = QtChart.QChartView(chart)

         self.chart_area.setContentsMargins(0, 0, 0, 0)
         layout.setContentsMargins(0, 0, 0, 0)

         self.addChartInLayout(chartview, layout)


    def addChartInLayout(self, newchartview, layout):
         count = self.chart_area_layout.count() + 1
         layout.insertWidget(count, newchartview, 100)


    def addReplaceChartInLayout(self, newchartview, layout):
         #Delete previus Chart or other that is occupying the layout.
         self.deleteItemsOfLayout(layout)

         count = self.chart_area_layout.count() - 1
         layout.insertWidget(count, newchartview)


    def deleteItemsOfLayout(self, layout):
         if layout is not None:
             while layout.count():
                 item = layout.takeAt(0)
                 widget = item.widget()
                 if widget is not None:
                     widget.setParent(None)
                 else:
                     self.deleteItemsOfLayout(item.layout())

"""
#Initiera UI-fönstret från designverktyget.
app = QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec())