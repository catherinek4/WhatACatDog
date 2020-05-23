import mysql.connector
import pandas as pd

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="your password"
)
cursor = db.cursor()
cursor.execute("create database whatacatdog")
db.close()

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="your password",
  database="whatacatdog"
)
cursor = db.cursor()

cats = pd.read_csv("csv/cats.csv", sep=',', header=None, dtype=None, encoding='utf-8')
dogs = pd.read_csv("csv/dogs.csv", sep=',', header=None, dtype=None, encoding='utf-8')

cursor.execute("create table cat (breed VARCHAR(255) PRIMARY KEY, name VARCHAR(255), weight VARCHAR(32), longevity_age VARCHAR(32), origin_country VARCHAR(64), wool_length VARCHAR(32), height VARCHAR(32), colors VARCHAR(255), history TEXT) ")
cursor.execute("create table dog (breed VARCHAR(255) PRIMARY KEY, name VARCHAR(255), height VARCHAR(128), weight VARCHAR(128), longevity_age VARCHAR(32), icfg VARCHAR(32), origin_country VARCHAR(32), colors VARCHAR(255), history TEXT)")
sql_c = "INSERT IGNORE INTO cat VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
sql_d = "INSERT IGNORE INTO dog VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

for dog in dogs.values:
  a = []
  a.append(dog[0])
  a.append(dog[1])
  a.append(dog[2])
  a.append(dog[3])
  a.append(dog[4])
  a.append(dog[5])
  a.append(dog[6])
  a.append(dog[8])
  a.append(dog[7])
  val = (a)
  cursor.execute(sql_d, val)
db.commit()

for cat in cats.values:
  a = []
  a.append(cat[0])
  a.append(cat[1])
  a.append(cat[2])
  a.append(cat[3])
  a.append(cat[4])
  a.append(cat[5])
  a.append(cat[6])
  a.append(cat[7])
  a.append(cat[8])
  val = (a)
  cursor.execute(sql_c, val)
db.commit()

print("db created")