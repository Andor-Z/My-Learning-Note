#SQLite
#表 通过外键关联
#操作关系数据库  链接到数据库 Connection
#打开游标 Cursor
import sqlite3
conn = sqlite3.connect('test.db')
#连接到数据库，文件为test.db，如果文件不存在，则自动在当前目录创建

#创建Cursor
cursor = conn.cursor()

#创建user表
cursor.execute('create table user(id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user(id, name) values(\'1\', \'Michael\')')
cursor.rowcount
#关闭Cursor
cursor.close()
#提交事务
conn.commit()
#关闭Connection
conn.close()
