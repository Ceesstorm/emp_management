import mysql.connector
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Mxstream12',
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE useit")

print("ALL DONE!")
