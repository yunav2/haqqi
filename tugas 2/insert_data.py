import mysql.connector

# database
db = mysql.connector.connect( 
  host="localhost",
  user="root",
  passwd="",
  database="hawqii"
)

cursor = db.cursor()
sql = "INSERT INTO user (name, email, no_handphone) VALUES (%s, %s, %s)"
# val = ("hawqii", "hawqi12@gmail.com", "081232912323")
# cursor.execute(sql, val)

# db.commit()

# print("{} done".format(cursor.rowcount))
values = [
    ("hawqii", "hawqi@gmail.com", "923023028"),
    ("ariwsto", "ariwsto@gmail.com", "923023028"),
    ("fawrus", "fawrus@gmail.com", "923023028"),
    ("baguws", "baguws@gmail.com", "923023028")
]

for val in values:
    cursor.execute(sql, val)
    db.commit()
    
print("{} done".format(len(values)))