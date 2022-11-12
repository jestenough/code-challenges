SELECT number,
    CASE WHEN number % 2 = 0 THEN number*8
        ELSE number*9
    END as res
FROM multiplication