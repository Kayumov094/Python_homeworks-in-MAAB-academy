print('Welcome to homework 15')
print("Arslonbek Xush kelibsiz")
import requests
import os
import json
import random
"""Create a new database with a table named Roster that has three fields: Name, Species, and Age.
 The Name and Species columns should be text fields, and the Age column should be an integer field."""

"""Roster nomli jadval bilan yangi ma'lumotlar bazasini yarating, unda uchta maydon mavjud: Ism, Tur va Yosh. 
Ism va Tur ustunlari matn maydonlari, Yosh ustuni esa butun son maydoni bo'lishi kerak."""
 
# sqlite3 modulini iport qilib oldim 
import sqlite3 # sqlite3 modulini import qilib oldim 

# conn = sqlite3.connect('roster.db') # sqlite3 moduli ichida connect() funksiyasi yordamida yangi roster.db file yaratdim 
# cursor = conn.cursor() # cursor() funksiyasi yordamida cursor objectini yaratdim 

# # conn va cursorlar yordamida SQL table create qilaman
# cursor.execute("""
# CREATE table if not exists roster (
#                name text,
#                type text,
#                age integer
#                )
# """)

# conn.commit() # o'zgarishlarni saqlayman
# conn.close() # roster.db file ga boglanishni yakunlayman

# endi cussor yordamida SQL sorovlarini barajaraman
# conn = sqlite3.connect('roster.db')
# cursor = conn.cursor()

# cursor.execute("Select * from roster")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)
# conn.close()
# print("Roster jadvalidan malumotlar chaqirib olindi")

 
 

# Benjamin Sisko	Inson	40
# Jadzia Dax	Trill	300
# Kira Neris	Bajoran	29

# yana roster.db bilan boglanaman
conn = sqlite3.connect('roster.db')
cursor = conn.cursor()
# data = [
#     ('Benjamin Sisko','Inson',	40),
#     ('Jadzia Dax','Trill',	300),
#     ('Kira Neris','Bajoran',29)
# ]

# cursor.executemany("Insert into roster (name, type, age) values(?,?,?)", data)
# conn.commit()
# cursor.execute("SELECT * FROM roster")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)
# conn.close()

# print(conn.in_transaction) # db ochiq yoki yopiqligini tekshiradi 

# cursor.execute("Update roster set name = 'Erzi Dax' where name = 'Jadzia Dax'")
# conn.commit()
# cursor.execute("SELECT * FROM roster")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)
 
cursor.execute("Select name, age from roster where type = 'Bajoran'")
rows = cursor.fetchall()
for row in rows:
    print(row)