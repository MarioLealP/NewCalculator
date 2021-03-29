import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Benylin",
  password="4zpHMhP5H5A*",
  database="calculator"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM FinalAnswer")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)