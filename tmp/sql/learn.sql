-- 4.19
-- 重复的电子邮箱
SELECT Email FROM
{
    SELECT Email, COUNT(Email) AS num
    FROM Person
    GRUOP BY Email
} AS statistic
WHERE num > 1
;
-- 自联结
SELECT DISTINCT a.Email FROM Person as a, Person AS b
WHERE a.Email = b.Email and a.Id != b.Id
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