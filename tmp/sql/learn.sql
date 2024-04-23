-- 4.23
-- 从不订购的客户
SELECT name FROM Customers AS 'Customers' 
FROM Customers
WHERE Customers.id NOT IN
(
    SELECT customerId FROM Orders
)
;

-- 温度上升的日期
-- 注意使用日期的函数判断今天和昨天
SELECT a.id 
FROM
    Weather AS a
    Weather AS b
WHERE
    datediff(a.recordDate, b.recordDate) AND a.Temperature > b.Temperature
;

-- 4.20
-- 重复的电子邮箱
-- 创建子表statistic
SELECT Email FROM
(
    SELECT Email, COUNT(Email) AS num
    FROM Person
    GROUP BY Email
 ) AS statistic
WHERE num > 1
;
-- 自联结
SELECT DISTINCT a.Email FROM Person as a, Person AS b
WHERE a.Email = b.Email and a.Id != b.Id
;

-- 删除重复的电子邮箱
DELETE p1 
FROM
    Person AS p1,
    Person AS p2
WHERE p1.Email = p2.Email AND p1.Id > p2.Id
;

-- 4.18
-- 超过经理收入的员工
SELECT 
    a.Name AS 'Employee'
FROM
    Employee AS a,
    Employee AS b
WHERE 
    a.ManagerId = b.id
        AND a.Salary > b.Salary
;