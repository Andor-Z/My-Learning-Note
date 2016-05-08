
  
###MySQL的启动和停止
- 图像化操作  
	windows服务（本地）中找到MySQL选择启动、暂停
- cmd操作  
	管理员运行cmd  
	net start mysql56  
	net stop mysql56


###1-4 登陆与退出  

#####MySQL登陆 
- 清屏：`cls`  
- 登陆：`mysql -uroot -p -P3306 -h127.0.0.1`  
	`-P`为端口，默认为3306；·`-h`为IP地址，默认为127.0.0.1本地回环地址。若都为本地默认，可以不写

- 输出版本信息并退出：`-V`  
##### MySQL退出  
  
- `mysql > exit;`
- `mysql > quit;`
- `mysql > \q;`  
| 参数  | 英文描述  | 中文描述  |  
| ----- | ---- | ---- |  
| -D    | --database=name | 打开指定数据库|  

###1-5修改mysql提示符
-连接客户端时通过参数指定  
`shell>mysql -uroot -p密码 --prompt 提示符`  
实操：`>mysql -uroot -p930716 --prompt \h`  
`\h`：服务器的名称  
-连接上客户端后通过prompt命令修改  
`mysql>prompt 提示符`  
实操：`prompt \u@\h \d>`  






###1-6mysql常用命令以及语法规范
####mysql常用命令
- 显示当前服务器版本  
- `SELECT VERSION();`  
- 显示当前日期时间  
- `SELECT NOW();`  
- 显示当前用户  
- `SELECT USER();`  


####mysql语句的规范


- **关键字与函数名称全部大写**  
- **数据库名称、表名称、字段名称全部小写**  
- SQL语句必须以**分号**结尾  
###1-7操作数据库
*`{}`必选项   
`|`选择其一   
`[]`可选项*   

  
- `CREATE  {DATABASE | SCHEMA} [IF NOT EXISTS] db_name [DEFAULF] CHARACTER SET [=] charset_name`   
	实操：`CREATE DATABSE t1;`  
	` [IF NOT EXISTS]`：假如创建的数据库已经存在，加入此语句可以忽略已经存在的数据库，但是会产生警告`Query OK,1 row affected,1 warning(0.00sec)`  


- 查看警告：`SHOW WARNING;`    
- 查看当前服务器下的数据表列表  
	`SHOW{DATABSES | SCHEMAS} [LIKE 'pattern' | WHERE expr]`
- 显示数据库创建时的指令：`SHOW CREATE DATABASE t1;`  

- `CREATE DATABASE IF NOT EXISTS t2 CHARACTER SET gbk;`

- 修改数据库：  
`ALTER {DATABASE | SCHEMA} [db_name] [DEFAULT] CHARACTER SET [=] charset-name`
- 删除数据库  
`DROP {DATABASE | SCHEMA} [IF NOT EXISTS] db_ name`

