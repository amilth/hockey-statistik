from mysql.connector import connect, Error
from PyQt5 import uic, QtChart
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
import sys


#Hämta in ui gränssnittet från designverktyget.
# class UI(QMainWindow):
class SEARCH(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("Python\\search_database.ui", self)

        # self.dBConn = None

        #Window.ButtonName.Event.RunThis
        # self.pushButtonConnectToDB.clicked.connect(self.ConnectToDB)
        # self.pushButtonDisconnectFromDB.clicked.connect(self.DisconnectFromDB)
        # self.pushButtonTopTenPlayers.clicked.connect(lambda: self.GetTop10Players(10))
        # self.pushButtonTopTenTeams.clicked.connect(lambda: self.GetTop10Teams(10))
        # self.pushButtonTopTenSalaries.clicked.connect(lambda: self.GetTop10Salaries(10))

    
    def skycake():
        print ("SkyCake evolves to stay just beyond the cognitive reach of " +
        "the bulk of men. SKYCAKE!!")

    
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
        
        chart_title= "Best players of all time"
        data = cursor.fetchall()
        SEARCH.addDataToTable(self, data)

        subData = [(x[0], x[2]) for x in data]
        
        SEARCH.deleteItemsOfLayout(self, self.chart_area_layout)
        SEARCH.addChartPie(self, subData, chart_title, self.chart_area_layout)


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

        chart_title= "Best teams of all time"
        data = cursor.fetchall()
        SEARCH.addDataToTable(self, data)

        subData = [(x[0], x[1]) for x in data]

        SEARCH.deleteItemsOfLayout(self, self.chart_area_layout)
        SEARCH.addChartStackedBar(self, subData, chart_title, self.chart_area_layout)


    def GetTop10Salaries(self, limit):

        if not self.dBConn:
            print("No connection found.")
            return
        
        cursor = self.dBConn.cursor()
        query = """ with lön as (
	                    SELECT s.PlayerName, max(s.Salary) as Salary
	                    FROM hockey.player_salaries as s
	                    group by s.PlayerName
                    ),
                    season as (
	                    SELECT s2.PlayerName, s2.Salary, s2.Season 
                        FROM hockey.player_salaries as s2
                    )
                    select lön.PlayerName
	                     , lön.Salary
                         , concat(left(min(s2.Season), 4), '-', right(max(s2.Season), 4)) as Seasons
                         , cast(right(max(s2.Season), 4) as SIGNED) - cast(left(min(s2.Season), 4) as SIGNED) as number_of_seasons
                    from lön
                    join season as s2 on s2.PlayerName = lön.PlayerName
                        and s2.Salary = lön.Salary
                    group by lön.PlayerName, lön.Salary
                    order by lön.Salary desc
                    limit %s;
                """
        cursor.execute(query, (limit,))

        self.tableWidgetTopTen.setColumnCount(len(cursor.column_names))
        self.tableWidgetTopTen.setRowCount(limit)
        self.tableWidgetTopTen.setHorizontalHeaderLabels(cursor.column_names)
        
        data = cursor.fetchall()
        SEARCH.addDataToTable(self, data)

        SEARCH.deleteItemsOfLayout(self, self.chart_area_layout)

        # Chart order is reversed. First chart will be placed at the bottom.
        chart_title= "Players with highest salaries of all time"
        subDataSalary = [(x[0], x[1]) for x in data]
        SEARCH.addChartStackedBar(self, subDataSalary, chart_title, self.chart_area_layout)
        
        chart_title= "Corresponding number of seasons"
        subDataSeasons = [(x[0], x[3]) for x in data]
        SEARCH.addChartStackedBar(self, subDataSeasons, chart_title, self.chart_area_layout)


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
        
        SEARCH.addChartInLayout(self, chartview, layout)


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

        SEARCH.addChartInLayout(self, chartview, layout)


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


#Initiera UI-fönstret från designverktyget.
# app = QApplication(sys.argv)
# window = UI()
# window.show()
# sys.exit(app.exec())