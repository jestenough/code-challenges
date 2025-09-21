DELETE FROM Person p1 USING Person p2
WHERE p1.id > p2.id AND p1.email = p2.email;