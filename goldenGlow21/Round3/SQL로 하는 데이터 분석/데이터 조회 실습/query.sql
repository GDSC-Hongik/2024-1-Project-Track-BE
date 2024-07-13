SELECT * 
FROM member 
WHERE (age BETWEEN 20 AND 29) AND (MONTH(sign_up_day) = 7);
