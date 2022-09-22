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
        self.addDataToTable(data)

        subData = [(x[0], x[2]) for x in data]
        
        self.deleteItemsOfLayout(self.chart_area_layout)
        self.addChartPie(subData, chart_title, self.chart_area_layout)
