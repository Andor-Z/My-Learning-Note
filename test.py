import mysql.connector

config = {
  'user': 'scott',
  'password': 'tiger',
  'host': '127.0.0.1',
  'database': 'employees',
  
}

cnx = mysql.connector.connect(**config)

cnx.close()