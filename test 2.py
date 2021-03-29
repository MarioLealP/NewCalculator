import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Benylin",
  password="4zpHMhP5H5A*",
  database="calculator"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM `FinalAnswer` WHERE id=(SELECT MAX(id) FROM `FinalAnswer`)");

myresult = mycursor.fetchone()

print(myresult)