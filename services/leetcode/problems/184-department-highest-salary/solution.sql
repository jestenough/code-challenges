SELECT d.name AS "Department", e.name AS "Employee", e.salary AS "Salary"
FROM Employee e
INNER JOIN Department d ON e.departmentId = d.id
WHERE (d.id, e.salary) IN (
    SELECT d.id, MAX(e.salary)
    FROM Employee e
    INNER JOIN Department d ON e.departmentId = d.id
    GROUP BY d.id
)
