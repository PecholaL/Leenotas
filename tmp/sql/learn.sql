-- 4.18
-- 超过经理收入的员工
SELECT 
    a.Name AS 'Employee'
FROM
    Employee AS a,
    Employee AS b
WHERE 
    a.ManagerId = b.ManagerId
        AND a.Salary > b.Salary
;