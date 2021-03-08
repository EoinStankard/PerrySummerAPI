import mysql.connector

db = mysql.connector.connect(
	user="root",
	password="root",
	host="localhost",
)

cursor=db.cursor()
cursor.execute("CREATE DATABASE perrySummer")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="perrySummer"
)
mycursor = mydb.cursor()
sqlUser="CREATE TABLE user (name VARCHAR(50),id VARCHAR(100))"
sqlMessage="CREATE TABLE message (fromID VARCHAR(100),toID VARCHAR(100),message TEXT(255),id VARCHAR(100), time DATETIME)"
mycursor.execute(sqlUser)
mycursor.execute(sqlMessage)