import mysql.connector

# database
db = mysql.connector.connect( 
  host="localhost",
  user="root",
  passwd="",
  database="hawqii"
)

cursor = db.cursor()
sql = "UPDATE user SET name=%s, email=%s, no_handphone=%s WHERE user_id=%s"
val = ("Fawri", "Fawri@gmail.com", "08123849022", 1)
cursor.execute(sql, val)

db.commit()

print("{} done".format(cursor.rowcount))