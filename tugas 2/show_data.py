import mysql.connector

# database
db = mysql.connector.connect( 
  host="localhost",
  user="root",
  passwd="",
  database="hawqii"
)

cursor = db.cursor()
sql = "SELECT * FROM user"
cursor.execute(sql)

results = cursor.fetchall()

for data in results:
    print(data)