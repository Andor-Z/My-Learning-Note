### 181. Employees Earning More Than Their Managers  
  
The `Employee` table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.  
  
```
+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+
```  
  
Given the `Employee` table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who earns more than his manager.  
  

```
+----------+
| Employee |
+----------+
| Joe      |
+----------+
``` 
  

### Solution(1)  

一张员工表，表里有`Id`和`ManagerId`，`ManagerId` 表示当前员工所归属主管的Id，求哪些员工挣的比他主管还多？  
  
- 思路  
在表1的`Id`等于表2的`ManagerId`的前提下，求表2中的`Salary`大于表一的员工  
  
```
SELECT e2.Name as Employee
FROM Employee as e1, Employee as e2
where  e1.Id = e2.ManagerId and e1.Salary < e2.Salary;
```  

### Solution(2)  
看了`Discuss` 发现还可以使用`join`方法：  
  
```
SELECT e2.Name as Employee
FROM Employee e1 JOIN Employee  e2 ON (e1.Id = e2.ManagerId)
where e1.Salary < e2.Salary;
```
  
`Discuss` 和我的印象的书里都是说用 `JOIN` 会比较好，好像是在多表查询的时会好点，这个题目某种程度上说还是单表查询。