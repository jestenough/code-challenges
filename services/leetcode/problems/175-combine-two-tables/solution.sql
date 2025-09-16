SELECT p.firstName, p.lastName, a.city, a.state
FROM Person as p
LEFT JOIN Address as a ON a.personId = p.personId