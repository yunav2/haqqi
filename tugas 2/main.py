import mysql.connector
import os

db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="",
  database="tugas3"
)


def insert_data(db):
  nama = input("Masukan nama: ")
  email = input("Masukan email: ")
  no_handphone = input("Masukan No Hp: ")
  val = (nama, email, no_handphone)
  cursor = db.cursor()
  sql = "INSERT INTO user (nama, email, no_handphone) VALUES (%s, %s, %s)"
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil disimpan".format(cursor.rowcount))


def show_data(db):
  cursor = db.cursor()
  sql = "SELECT * FROM user"
  cursor.execute(sql)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)


def update_data(db):
  cursor = db.cursor()
  show_data(db)
  id = input("pilih id user> ")
  nama = input("Nama baru: ")
  email = input("Email baru: ")
  no_handphone = input("No_Handphone baru: ")

  sql = "UPDATE user SET nama=%s, email=%s, no_handphone=%s WHERE id=%s"
  val = (nama, email, no_handphone, id)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil diubah".format(cursor.rowcount))


def delete_data(db):
  cursor = db.cursor()
  show_data(db)
  id = input("pilih id user> ")
  sql = "DELETE FROM user WHERE id"
  val = (id)
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil dihapus".format(cursor.rowcount))


def search_data(db):
  cursor = db.cursor()
  keyword = input("Kata kunci: ")
  sql = "SELECT * FROM user WHERE nama LIKE %s OR email LIKE %s"
  val = ("%{}%".format(keyword), "%{}%".format(keyword))
  cursor.execute(sql, val)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)


def show_menu(db):
  print("=== APLIKASI DATABASE PYTHON ===")
  print("1. Insert Data")
  print("2. Tampilkan Data")
  print("3. Update Data")
  print("4. Hapus Data")
  print("5. Cari Data")
  print("0. Keluar")
  print("------------------")
  menu = input("Pilih menu> ")

  #clear screen
  os.system("clear")

  if menu == "1":
    insert_data(db)
  elif menu == "2":
    show_data(db)
  elif menu == "3":
    update_data(db)
  elif menu == "4":
    delete_data(db)
  elif menu == "5":
    search_data(db)
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")


if __name__ == "__main__":
  while(True):
    show_menu(db)