### 182. Duplicate Emails  
  
Write a SQL query to find all duplicate emails in a table named `Person`.    

```
+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
```  

For example, your query should return the following for the above table:  


```
+---------+
| Email   |
+---------+
| a@b.com |
+---------+
```  

Note: All emails are in lowercase.  


### 答案1： 

```sql
SELECT distinct p1.Email 
FROM Person as p1,Person as p2 
WHERE p1.Id != p2.Id and p1.Email = p2.Email ;
```
  

### 答案2：  

```
SELECT Email 
FROM Person 
GROUP BY Email 
HAVING COUNT(Email) > 1;
```
  

思路： 
本来是准备直接用`GROUP BY`的，但是没想起来怎么加条件，也就是`HAVING`，后来用单表查询感觉语句太长了，翻了下书，找到了HAVING。 
> `HAVING`子句中的谓词在`GROUP BY`形成分组后才起作用  
> `HAVING`子句中的条件应用到每个分组上，不满足`HAVING`子句谓词的分组将被抛弃  