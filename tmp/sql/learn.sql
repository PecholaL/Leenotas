-- 4.25
-- 所有用户第一次登录的日期
SELECT a.player_id, MIN(a.event_date) AS 'first_login'
FROM Activity AS a
GROUP BY a.player_id
;

-- 奖金少于1000的员工姓名及奖金
-- 左连接
SELECT name AS 'name', bonus AS 'bonus'
FROM Employee LEFT JOIN Bonus
ON Employee.empId=Bonus.empId
WHERE bonus IS null or bonus<1000
;

-- 寻找用户推荐人
-- 找出没有被id=2的客户推荐的客户姓名
SELECT name AS 'name'
FROM Customer
WHERE referee_id IS null or referee_id!=2
;

-- 订单最多的客户
SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1
;
-- 研究了半天笨办法，语法不厚道
SELECT customer_number
FROM
(
    SELECT customer_number, COUNT(*) AS count
    FROM Orders
    GROUP BY customer_number
) AS statistic
WHERE count=
(
    SELECT MAX(count) 
    FROM 
    (
        SELECT customer_number, COUNT(*) AS count
        FROM Orders
        GROUP BY customer_number
    ) AS statistic
)
;


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
    datediff(a.recordDate, b.recordDate)=1 AND a.Temperature > b.Temperature
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
WHERE a.Email = b.Email AND a.Id != b.Id
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