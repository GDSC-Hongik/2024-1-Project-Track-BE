SELECT
    MAX(copang_report.price) AS max_price,
    AVG(copang_report.star) AS avg_star,
    COUNT(DISTINCT(copang_report.email)) AS distinct_email_count
FROM (SELECT price, star, email
FROM item AS i INNER JOIN review AS r ON r.item_id = i.id
INNER JOIN member AS m ON r.mem_id = m.id) 
AS copang_report;