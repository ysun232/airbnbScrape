#the working version of adding information into mysql database


import pymysql
from needMOre.airbnbFinal import *

mydb = pymysql.connect(
    host="",
    user="",
    passwd="",
    database=""
)
mycursor = mydb.cursor()

sql1 = "Insert into airbnb(title, price, description, takenTime) values (%s,%s,%s,%s)"
val1 = newTuple
mycursor.executemany(sql1, val1)

mydb.commit()