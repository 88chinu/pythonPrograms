# import sqlite3

# coun = sqlite3.connect("college.db")
# cursor = coun.cursor()
# print("db Connected")

# cursor.execute(""" CREATE TABLE IF NOT EXISTS STUDENTS
# (SIC INTEGER PRIMERYKEY,
# NAME VRCHAR(15),
# AGE INTEGER,
# COURSE VARCHAR(20))
# """)

# # cursor.execute("""INSERT INTO STUDENTS(SIC, NAME, COURSE, AGE)VALUES
# # (2345,"CHINMAYA","MCA", 22),(2346,"NIRMAL","MCA", 22)""")

# name= input("Enter name: ")
# sic= int(input("Enter sic: "))
# age= int(input("Enter age: "))
# course= input("Enter course: ")
# cursor.execute("""INSERT INTO STUDENTS(NAME,SIC,AGE,COURSE)VALUES(?,?,?,?)""",
# (name,sic,age,course))

# cursor.execute("""SELECT * FROM STUDENTS""")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# coun.commit()