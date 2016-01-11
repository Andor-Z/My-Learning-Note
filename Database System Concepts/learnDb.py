import mysql.connector as mysqlcon

# port  数字  MySQL服务器端口号
# charset  字符串 连接编码
config = {
	'user': 'root', 
	'password': '930716', 
	'host': '127.0.0.1', 
	'database': 'cpt_db_learn'
}
con = mysqlcon.connect(**config)

con.close()

