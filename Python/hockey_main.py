from mysql.connector import connect, Error
from PyQt5 import uic, QtChart
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
import sys


#Hämta in ui gränssnittet från designverktyget.
class UI(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("Python\\main_ui_window.ui", self)

        self.dBConn = None

        #Window.ButtonName.Event.RunThis
        self.pushButtonConnectToDB.clicked.connect(self.ConnectToDB)
        self.pushButtonDisconnectFromDB.clicked.connect(self.DisconnectFromDB)
        self.pushButtonTopTenPlayers.clicked.connect(lambda: self.GetTop10Players(10))
        self.pushButtonTopTenTeams.clicked.connect(lambda: self.GetTop10Teams(10))
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
        if not self.dBConn:
            print('Disconnected from MySQL database.')
            sys.exit(app.exec())


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
        
        data = cursor.fetchall()
        self.AddDataToTable(data)
        self.ShowChartPie(data)


    def GetTop10Teams(self, limit):
        if not self.dBConn:
            print("No connection found.")
            return
        
        cursor = self.dBConn.cursor()
        query = """SELECT t.TeamName as 'Team' 
                        , count(g.ScoringTeamId) as 'Number of matches won'
                    FROM hockey.event_goal as g
                    join hockey.team as t on t.TeamId = g.ScoringTeamId
                    group by g.ScoringTeamId
                    order by count(g.ScoringTeamId) desc
                    limit %s;"""
        cursor.execute(query, (limit,))

        self.tableWidgetTopTen.setColumnCount(len(cursor.column_names))
        self.tableWidgetTopTen.setRowCount(limit)
        self.tableWidgetTopTen.setHorizontalHeaderLabels(cursor.column_names)
        
        data = cursor.fetchall()
        self.AddDataToTable(data)
        self.ShowChartStackedBar(data)


    def AddDataToTable(self, data):
        for rowNum, rowData in enumerate(data):
            for colNum, colData in enumerate(rowData):
                self.tableWidgetTopTen.setItem(rowNum, colNum, QTableWidgetItem(str(colData)))
        
            
    def ShowChartPie(self, data):
        players = [x[0] for x in data]
        goals = [x[2] for x in data]

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
        chart.setTitle("Best players of all time")
        chart.legend().setAlignment(Qt.AlignLeft)
        chart.setAnimationOptions(QtChart.QChart.SeriesAnimations)
        chart.setTheme(QtChart.QChart.ChartTheme.ChartThemeQt)

        chartview = QtChart.QChartView(chart)

        self.chart_area.setContentsMargins(0, 0, 0, 0)
        self.chart_area_layout.setContentsMargins(0, 0, 0, 0)
        
        self.addReplaceChartInLayout(chartview, self.chart_area_layout)


    def ShowChartStackedBar(self, data):
        
        teams = [x[0] for x in data]
        goals = [x[1] for x in data]

        series = QtChart.QBarSeries()
        for x in teams:
            setattr(self, "set"+str(x), QtChart.QBarSet(str(x)))
            series.append(getattr(self, "set"+str(x)))
            getattr(self, "set"+str(x)).append(goals[teams.index(x)])

        chart = QtChart.QChart()
        chart.addSeries(series)
        chart.setTitle("Best teams of all time")
        chart.setAnimationOptions(QtChart.QChart.SeriesAnimations)

        categories = ["Goals"]
        axis = QtChart.QBarCategoryAxis()
        axis.append(categories)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)
        chart.legend().setAlignment(Qt.AlignLeft)

        chartview = QtChart.QChartView(chart)

        self.chart_area.setContentsMargins(0, 0, 0, 0)
        self.chart_area_layout.setContentsMargins(0, 0, 0, 0)

        self.addReplaceChartInLayout(chartview, self.chart_area_layout)


    def addReplaceChartInLayout(self, newchartview, layout):
        #Delete previus Chart or other that is occupying the layout.
        self.deleteLaterGroupBox(layout)

        count = self.chart_area_layout.count() - 1
        layout.insertWidget(count, newchartview)


    def deleteLaterGroupBox(self, layout):
        count = layout.count()
        if count == 0:
            return
        item = layout.itemAt(count - 1)
        widget = item.widget()
        widget.deleteLater()


#Initiera UI-fönstret från designverktyget.
app = QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec())