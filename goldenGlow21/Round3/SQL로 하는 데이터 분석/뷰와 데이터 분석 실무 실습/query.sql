DESCRIBE employee;
CREATE VIEW v_emp AS 
    SELECT id,
           name,
           age, 
           department, 
           phone_num, 
           hire_date 
    FROM employee;
SELECT * 
FROM v_emp;
