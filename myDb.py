import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'password'
	)

#Prepare a cursor object
cursorobject = dataBase.cursor()

#create a database
cursorobject.execute("CREATE DATABASE dcrm")

print("All Done")