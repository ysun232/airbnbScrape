import pymysql


mydb = pymysql.connect(
    host="",
    user="",
    passwd="",
    database=""
)
mycursor= mydb.cursor()

mycursor.execute("Create table airbnb(id INT AUTO_INCREMENT PRIMARY KEY, title varchar(255), price varchar (255), description varchar (255), takenTime DATETIME)")

mydb.commit()