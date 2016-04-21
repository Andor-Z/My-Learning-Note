#MYSQL必知必会
SHOW DATABASES;
SHOW TABLES;
SHOW COLUMNS FROM customers;
#DESCRIBE customers; = SHOW COLUMNS FROM customers;
SHOW STATUS  #用于显示广泛的服务器状态信息；
SHOW CREATE DATABASE
SHOW CREATE TABLE
SHOW GRANTS #显示授权用户的安全权限
SHOW ERRORS   SHOW WARNINGS #显示服务器错误或警告消息
HELP SHOW
INFORMA-TION_SCHEMA  #获得和过滤模式信息


USE mysqlbizhibihui;


#C4数据检索

SELECT prod_name FROM products; 
SELECT prod_id,prod_name,prod_price FROM products;
SELECT * FROM products;

#检索不同的行
SELECT vend_id
FROM products;

SELECT DISTINCT vend_id
FROM products;  #只返回不同的值，DISTINCT 不能部分使用，它会用用于所有列，而不是仅前置它的列

#限制结果LIMIT
SELECT prod_name
FROM products
LIMIT 5;  #LIMIT指示MySQL返回不多于5行

SELECT prod_name
FROM products
LIMIT 5,5; #返回从第5行开始取5行

#带一个值的LIMIT总是从第一行开始，给出的书为返回的行数。
#带两个值的LIMIT可以指定从行号为第一个只的位置开始
#行0  检索出来的第一行为行0而不是行1，因此，LIMIT 1，1检索出来第二行而不是第一行
LIMIT 4 OFFSET 3 #从行3开始取4行

#完全限定的表名
SELECT products.prod_name
FROM products;

#C5排序检索数据

SELECT prod_name
FROM products
ORDER BY prod_name;

SELECT prod_id,prod_price,prod_name
FROM products
ORDER BY prod_price,prod_name;

SELECT prod_id
FROM products
ORDER BY prod_price,prod_name;

#降序排列DESC
SELECT prod_id,prod_price,prod_name
FROM products
ORDER BY prod_price DESC;  

SELECT prod_id,prod_price,prod_name
FROM products
ORDER BY prod_price DESC，pro_name DESC;  #多列降序排列DESC

#使用ORDER BY和LIMIT的组合，找出一个列中最高或者最低额值。
SELECT prod_price
FROM products
ORDER BY prod_price DESC
LIMIT 1;


#C6过滤数据
#同时使用ORDER BY和WHERE子句时，应该让ORDER BY位于WHERE之后
SELECT prod_name,prod_price
FROM products
WHERE prod_price = 2.50;

SELECT prod_name,prod_price
FROM products
WHERE prod_name = 'fuses';

SELECT prod_name,prod_price
FROM products
WHERE prod_price<= 10;


SELECT vend_id ,prod_name
FROM products
WHERE vend_id <> 1003;

SELECT vend_id ,prod_name
FROM products
WHERE vend_id != 1003;


SELECT prod_name, prod_price
FROM products
WHERE prod_price BETWEEN 5 AND 10;

#NULL无值（no value）
#检查空值 IS NULL子句
SELECT prod_name,prod_price
FROM products
WHERE prod_price IS NULL;

SELECT cust_id
FROM customers
WHERE cust_email IS NULL;


#C7数据过滤

SELECT prod_id,prod_price,prod_name
FROM products
WHERE vend_id = 1003 AND prod_price <= 10;

SELECT prod_name,prod_price
FROM products
WHERE vend_id = 1002 OR vend_id = 1003;

#OR和AND一起优先处理AND

SELECT prod_name,prod_price
FROM products
WHERE vend_id = 1002 OR vend_id = 1003 AND prod_price >= 10;

SELECT prod_name,prod_price
FROM products
WHERE (vend_id = 1002 OR vend_id= 1003) AND prod_price >= 10;

#IN操作符
#IN与OR具有相同的功能
SELECT prod_name, prod_price
FROM products
WHERE vend_id IN (1002, 1003)
ORDER BY prod_name;

# 7.3 NOT 操作符
## WHERE子句中用来否定它之后所跟的任何条件
SELECT prod_name, prod_price,vend_id
FROM products
WHERE vend_id NOT IN (1002,1003)
ORDER BY prod_name;

##EXISTS?

#C8 用通配符（wildcard）进行过滤
###schema和pattern都翻译成“模式”

## 8.1.1 （%）任何字符出现任意次数
SELECT prod_id, prod_name
FROM products
WHERE prod_name LIKE 'jet%';

SELECT prod_id, prod_name
FROM products
WHERE prod_name LIKE '%anvil%';

###'%'不能匹配NULL

###下划线（_）匹配单个字符

SELECT prod_id, prod_name
FROM products
WHERE prod_name LIKE '_ TON ANVIL';

###通配符速度较慢，不要过度使用通配符


# C9 正则表达式：用来匹配文本的特殊的串（字符集合）

SELECT prod_name
FROM products
WHERE prod_name REGEXP'1000'
ORDER BY prod_name;

SELECT prod_name
FROM products
WHERE prod_name REGEXP '.000'
ORDER BY prod_name;

###'.'是正则表达式中一个特殊的字符，它表示匹配任意一个字符
###MYSQL中正则表达式不区分大小写，若需区分大小写，使用**BINARY**
###如 WHERE prod_name REGEXP BINARY 'JetPack .1000'

##9.2.2 正则OR的操作符 ‘|’
SELECT prod_name
FROM products
WHERE prod_name REGEXP '1000|2000'
ORDER BY prod_name;


SELECT prod_name
FROM products
WHERE prod_name REGEXP '1000|2000|3000'
ORDER BY prod_name;

##[]
SELECT prod_name
FROM products
WHERE prod_name REGEXP '[123] Ton'
ORDER BY prod_name;
###这句正则表达式‘[123] Ton的意思是匹配1或2或3，因此，匹配1 ton和2 Ton 以及3 Ton

SELECT prod_name
FROM products
WHERE prod_name REGEXP '1|2|3 Ton'
ORDER BY prod_name;
###这句的意思是匹配1、2、3 Ton

##…^否定已给字符集 [^123]匹配除这些字符外的任何东西

## 9.2.4 匹配范围
###匹配数字0到9：[0123456789] 简化 [0-9]
SELECT prod_name
FROM products
WHERE prod_name REGEXP '[1-5] Ton'
ORDER BY prod_name;

## 9.2.5 匹配特殊字符
###'\\'  \\-表示查找-， \\.表示查找.。  '\\\'表示查找'\'  转义（escaping）
SELECT vend_name
FROM vendors
WHERE vend_name REGEXP '\\.'
ORDER BY vend_name;

###\\也用来引用元字符（具有特殊含义的字符）
###\\f  换页    \\n   换行   '\\r'回车   '\\t'制表  '\\v'纵向制表
###重复元字符
### '*' 0个或多个匹配   '+' 1个或多个匹配（等于{1,}）   '?'  0个或1个匹配（{0,1}）   
### '{n}'  指定数目的匹配     '{n,}'不少于指定数目的匹配   '{n, m}'匹配数目的范围（m不超过255）

SELECT prod_name
FROM products
WHERE prod_name REGEXP '\\([0-9] sticks?\\)'
ORDER BY prod_name;

SELECT prod_name
FROM products
WHERE prod_name REGEXP '[[:digit:]]{4}'
ORDER BY prod_name;
###'{4}'确切地要求它前面的字符（任意数字）出现4次

###
SELECT prod_name
FROM products
WHERE prod_name REGEXP '[0-9][0-9][0-9][0-9]'
ORDER BY prod_name;

##9.2.8 定位符

SELECT prod_name
FROM products
WHERE prod_name REGEXP '^[0-9\\.]'
ORDER BY prod_name;

###'^' 在集合中（[]）表示否定该集合，在其他场合表示定位文本的开始
###'$' 文本的结尾


# C10 创建计算字段
###字段（field） 基本上于列相同

## 10.2 拼接（concatenate）

SELECT Concat(vend_name,'(',vend_country,')')
FROM vendors
ORDER BY vend_name;

###删除数据右侧多余的空格来整理数据RTrim   左侧 LTrim   两侧  Trim

SELECT Concat(RTrim(vend_name),'(',RTrim(vend_country),')')
FROM vendors
ORDER BY vend_name;

### 别名（alias）一个字段或值得替换名   AS赋值  有时也被称作导出列（derived column）
SELECT Concat(RTrim(vend_name),'(',RTrim(vend_country),')') AS vend_title
FROM vendors
ORDER BY vend_name;

## 10.3算术计算
SELECT prod_id, quantity, item_price, quantity*item_price AS expanded_price
FROM orderitems
WHERE order_num = 20005;

SELECT now();   ###显示当前日期


# C11 使用数据处理函数
##11.2.1 文本处理函数


###Upper()将文本转换为大写
SELECT vend_name, Upper(vend_name) AS vend_name_upcase
FROM vendors
ORDER BY vend_name;

SELECT cust_name,cust_contact
FROM customers
WHERE cust_contact = 'Y.Lie'


SELECT cust_name,cust_contact
FROM customers
WHERE soundex(cust_contact) = soundex('Y.Lie')

SELECT cust_id, order_num
FROM orders 
WHERE date(order_date) = '2005-09-01';


SELECT cust_id, order_num
FROM orders
WHERE Date(order_date) BETWEEN '2005-09-01' AND '2005-09-30';

SELECT cust_id, order_num
FROM orders
WHERE Year(order_date) = 2005 AND Month(order_date) = 9;

#C12 汇总数据

##聚集函数（aggregate function）

##12.2聚集不同值
SELECT AVG(DISTINCT prod_price) AS avg_price
FROM products
WHERE vend_id = 1003;

##12.3 组合聚集函数
SELECT COUNT(*) AS num_items,
	   MIN(prod_price) AS price_min,
	   MAX(prod_price) AS prod_max,
	   AVG(prod_price) AS price_avg
	   FROM products;



# C13 分组数据
SELECT vend_id, COUNT(*) AS num_prods
FROM products
GROUP BY vend_id;

###GROUP BY 必须出现在WHERE之后， ORDER BY 之前

###WITH ROLLUP
SELECT vend_id, COUNT(*) AS num_prods
FROM products
GROUP BY vend_id WITH ROLLUP;


SELECT vend_id, COUNT(*) AS num_prods
FROM products
GROUP BY vend_id WITH ROLLUP
HAVING num_prods >=3;

SELECT cust_id, COUNT(*) AS orders
FROM orders
GROUP BY cust_id
HAVING COUNT(*) >= 2;

###HAVING 与WHERE的区别：WHERE在数据分组前进行过滤，HAVING在数据分组后进行过滤

SELECT order_num, SUM(quantity*item_price) AS ordertotal
FROM orderitems
GROUP BY order_num
HAVING SUM(quantity*item_price) >= 50
ORDER BY (quantity*item_price);

#C14 使用子查询
### 查询（query） 
### 子查询（subquery) 嵌套在其他查询中的查询

SELECT order_num
FROM orderitems
WHERE prod_id = 'TNT2';
#上句输出order_num 20005,20007
SELECT cust_id
FROM orders
WHERE order_num IN (20005,20007);


SELECT cust_id
FROM orders
WHERE order_num IN (SELECT order_num
						   FROM orderitems
						   WHERE prod_id = 'TNT2');

###在SELECT语句中，子查询总是从内向外处理


#C15 联结表（join）

SELECT vend_name, prod_name, prod_price
FROM vendors, products
WHERE vendors.vend_id = products.vend_id
ORDER BY vend_name, prod_name;
###WHERE 子句实际上是作为过滤条件
###笛卡尔积（cartesian product） 由没有联结条件的表关系返回的结果
###检索出的行的数目将是第一个表中的行数乘以第二个表中的行数

##内部联结=等值联结（equijoin），基于两个表之间的相等测试

SELECT vend_name, prod_name, prod_price
FROM vendors INNER JOIN products
ON vendors.vend_id = products.vend_id;
#与前面一句返回完全相同的数据

##联结过个表
SELECT prod_name, vend_name, prod_price, quantity
FROM orderitems, products, vendors
WHERE products.vend_id = vendors.vend_id
  AND orderitems.prod_id = products.prod_id
  AND order_num = 20005
 ORDER BY quantity;
##基于性能考虑，不要联结不必要的表，联结的表越多，性能下降的越厉害

SELECT cust_name, cust_contact
FROM customers, orders,orderitems
WHERE orderitems.prod_id = 'TNT2'
AND orders.cust_id = customers.cust_id
AND orders.order_num = orderitems.order_num;

# C16 创建高级联结
###表别名  列别名
## - 等值联结
## - 自然联结
## - 自联结
## - 外部链接

##C16.2.1 自联结
SELECT prod_id, prod_name
FROM products
WHERE vend_id = (SELECT vend_id 
					FROM products
					WHERE prod_id = 'DTNTR');


SELECT p1.prod_id, p1.prod_name
FROM products AS p1, products AS p2
WHERE p2.prod_id = 'DTNTR'
AND p1.vend_id = p2.vend_id;


##C16.2.2 自然联结
SELECT c.*, o.order_num, o.order_date, oi.prod_id, oi.quantity, oi.item_price
FROM customers AS c, orders AS o, orderitems AS oi
WHERE c.cust_id = o.cust_id
AND oi.order_num = o.order_num
AND prod_id = 'FB';

SELECT c.cust_id, c.cust_name, COUNT(o.cust_id) AS num_ord
FROM orders AS o, customers AS c
WHERE o.cust_id = c.cust_id
GROUP BY cust_id;

SELECT c.cust_id, o.order_num
FROM customers AS c INNER JOIN orders AS o
ON c.cust_id = o.cust_id;

## - 外部联结
### LEFT OUTER JOIN  与 RIGHT OUTER JOIN
###外部联结是表示指定包括其所有行的表

SELECT c.cust_id, c.cust_name, COUNT(o.cust_id) AS num_ord
FROM orders AS o, customers AS c
WHERE o.cust_id = c.cust_id
GROUP BY cust_id;

###使用通常的联结，无法显示出无数据行，使用外部联结可以
SELECT c.cust_id, c.cust_name, COUNT(o.cust_id) AS num_ord
FROM orders AS o RIGHT OUTER JOIN customers AS c
ON o.cust_id = c.cust_id
GROUP BY cust_id;

# C17 组合查询（compound query） or  并（union）

### UNION
SELECT vend_id, prod_id, prod_price
FROM products
WHERE prod_price <= 5
UNION
SELECT vend_id, prod_id, prod_price
FROM products
WHERE vend_id IN (1001,1002);

#等同于（多条WHERE子句）
SELECT vend_id, prod_id, prod_price
FROM products
WHERE prod_price <= 5
OR vend_id in (1001,1002);

#> UNION中的每个查询必须包含相同的列、表达式或聚集函数（不过各个列不需要以相同的次序列出
### ？尝试使用不同次序列出，结果导致后一个SELECT的以自己的次序输出，导致表头与后续表体不符

## 17.2.3 包含或取消重复的行
### UNION 默认从查询结果集中自动去除了重读的行

### UNION ALL 返回所有匹配列

###组合查询中的排序，只能在最后一条SELECT语句之后，只能使用一条ORDER BY

# C18 全文搜索
### MyISAM 支持全文本搜索     InnoDB 不支持全文本搜索

### FULLTEXT 索引
### 不要再导入数据时使用FULLTEXT 更新索引需要时间，当导入数据到一个新表中时
### 应该先导入所有数据，然后再修改表，定义FULLTEXT

##全文本搜索  Match()指定被搜索的列  Against()  指定要使用的琐事表达式


SELECT note_text
FROM productnotes
WHERE MATCH(note_text) against('rabbit');

### s传递给match（）的值必须与FULLTEXT()定义中的相同，如果指定多个列，则必须列出它们（次序正确）
### 必须使用 BINARY才区分大小写

SELECT note_text
FROM productnotes
WHERE note_text LIKE '%RABBIT%';

###全文本搜索的一个重要部分就是对结果排序

SELECT note_text,
	match(note_text) against('rabbit') AS rank
	FROM productnotes;

##查询扩展
SELECT note_text
FROM productnotes
WHERE match(note_text) against('anvils');

SELECT note_text
FROM productnotes
WHERE match(note_text) against('anvils' WITH QUERY EXPANSION);

##布尔文本搜索   **即使没有FULLTEXT索引也可以使用** 但是操作的速度非常缓慢
SELECT note_text
FROM productnotes
WHERE match(note_text) against('heavy' IN BOOLEAN MODE);

###包含heavy但不包含任意以rope开始的词
SELECT note_text
FROM productnotes
WHERE match(note_text) against('heavy -rope*' IN BOOLEAN MODE);

###C19 插入数据 INSERT
INSERT INTO customers
VALUES(NULL,
'Pep E.LaPew',
'100 Main Street',
'Los Angeles',
'CA',
'90046',
'USA',
NULL,
NULL);

INSERT INTO customers(cust_name,
cust_address,
cust_city,
cust_state,
cust_zip,
cust_country,
cust_contact,
cust_email)
VALUES('Pep E.LaPew',
'100 Main Street',
'Los Angeles',
'CA',
'90046',
'USA',
NULL,
NULL);




#C23.存储过程
DELIMITER //

DELIMITER ;

DELIMITER //
CREATE PROCEDURE productpricing()
BEGIN
	SELECT AVG(prod_price) AS priceaverage
	FROM products;
END//
DELIMITER ;
#调用存储过程
CALL productpricing();

DROP PROCEDURE productpricing;  -- 注意无()
DROP PROCEDURE IF EXISTS productpricing;


DELIMITER //
CREATE PROCEDURE productpricing(
	OUT pl DECIMAL(8,2),
	OUT ph DECIMAL(8,2),
	OUT pa DECIMAL(8,2)
	)
BEGIN
	SELECT MIN(prod_price)
	INTO pl
	FROM products;
	SELECT MAX(prod_price)
	INTO ph
	FROM products;
	SELECT AVG(prod_price)
	INTO pa
	FROM products;
END//
DELIMITER ;

CALL productpricing(@pricelow,
					@pricehigh,
					@priceaverage);  --指定变量名，所有MySQL变量都必须以@开始。

SELECT @priceaverage;



DELIMITER //
CREATE PROCEDURE ordertotal(
IN onumber INT,
OUT ototal DECIMAL(8,2)
)
BEGIN
	SELECT SUM(item_price*quantity)
	FROM orderitems
	WHERE order_num = onumber
	INTO ototal;
END//
DELIMITER ;

CALL ordertotal(20005, @total);
SELECT @total;



#C24 游标（cursor）
 













