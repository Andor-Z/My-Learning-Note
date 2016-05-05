# C3.SQL语句

`DISTINCT` 去重
### 3.3.2 多关系查询
- 理解查询语句：先`from`，然后`where`，最后`select`。

```sql
SELECT name, course_id 
FROM instructor, teaches 
WHERE instructor.ID = teaches.ID;
```

### 3.3.3 自然连接(natural join)

- 上面一句可以使用 `natural join` 更简洁
```sql
SELECT name, course_id
FROM instructor NATURAL JOIN teaches;

```

- 可以使用自然连接将多个关系连接在一起
- 查询“列出教师的名字以及他们所讲授课程的名称”
```sql
SELECT name, title
FROM instructor natural join teaches, course
WHERE teaches.course_id = course.course_id
```

- 下面的自然连接不会出现相同的计算结果
```sql
SELECT name, title
FROM instructor NATURAL JOIN  teaches NATURAL JOIN course;
```
这是因为`instructor`和`course`两个表中不仅共同包含`course_id`这列，同时包含了`dept_name`，故这个查询语句会忽略那些教师所讲授的课程不是他所在系的课程。

- 指定相等列的自然连接`join ... using ()`
```sql
SELECT name, title
FROM (instructor NATURAL JOIN teaches) JOIN course USING (course_id);
```
这样就是查询“列出教师的名字以及他们所讲授课程的名称”

## 3.4 附加的基本运算
### 3.4.1 更名 `as`
 **表别名** table alias
### 3.4.2 字符串运算
- 字符串中若有单引号，则需要使用2个单引号表示，因为SQL使用一对单引号表示字符串
- 字符串上的相等运算是大小写敏感的，但是MySQL和SQL server是**不敏感的**
> `upper()`转换为大写
> `lower()`
> `trim()`去掉字符串后面的空格

- 匹配`like`
    - (%) 匹配任何字符串
    - (_)下划线，匹配任意一个字符
    - (\\)反斜线，转义字符

### 3.4.4 显示次序`order by`
- 降序 `desc`
- 升序`asc`

### 3.4.5 where 子句谓词
- `between``not between`

## 3.5 集合运算
- `union`并

```sql
(SELECT course_id
FROM section
WHERE semester = 'Fall' AND year = 2009)
UNION
(SELECT course_id
FROM section
WHERE semester = 'Spring' AND year = 2010
);
```
> `union`运算自动去重
> 若需保留重复，使用`union all` 替代`union`

- `intersect` 交
> ** MySQL 不支持**
> 使用方法和 *并* 一样
> 自动去重
> 若需保留重复，使用`intersect all` 替代

- `excpt`差
> ** MySQL 不支持**
`MySQL 可以使用left join`
## 3.7 聚集函数
- 平均值：`avg`
- 最小值：`min`
- 最大值：`max`
- 总和：  `sum`
- 计数：  `count`

### 3.7.2 分组聚类`group by`


having
嵌套子查询： in , not in






```sql

```