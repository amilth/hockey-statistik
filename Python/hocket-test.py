from mysql.connector import connect, Error

print("") #New line to better se where the code starts.


def ConnectToDB():
    """Connect to MySQL database

    Returns:
        conn: connection object
    """
    try:
        conn = connect(
            host="185.157.160.111",
            port="33306",
            user="my_db_admin",
            password="mysql",
            database="hockey"
        )
        
        if conn.is_connected():
            print('Connected to MySQL database')
            return conn
    
    except Error as err:
        print(err)


def DisconnectFromDB(conn):
    """Disconnect from MySQL database

    Args:
        conn: connection object
    """
    conn.close()
    print('Disconnected from MySQL database')


def GetTop10FromTable(conn, table):
    """Get top 10 players from table

    Args:
        conn: connection object
        table: table name
    """
    cursor = conn.cursor()
    cursor.execute("SELECT PlayerName FROM " + table + " LIMIT 10")
    return cursor.fetchall()


dbConn = ConnectToDB()
print(GetTop10FromTable(dbConn, "player"))
DisconnectFromDB(dbConn)