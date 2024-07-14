import mysql.connector

# database
db = mysql.connector.connect( 
  host="localhost",
  user="root",
  passwd="",
  database="hawqii"
)

# buat tabel didalam database
cursor = db.cursor()
sql = """CREATE TABLE user (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    no_handphone INT(25)
)"""
    
cursor.execute(sql) #menjalankan buat tabel

print("Done")