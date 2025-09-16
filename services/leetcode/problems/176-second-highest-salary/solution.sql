SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    OFFSET 1 LIMIT 1
) AS "SecondHighestSalary";
