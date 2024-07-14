import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

# if db.is_connected(): buatt ngecek terrhubung / engga ke database
#     print("yeayyyy")
