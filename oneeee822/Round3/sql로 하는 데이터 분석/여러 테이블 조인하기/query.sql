SELECT YEAR(i.registration_date) AS '등록 연도',
    COUNT(*) AS '리뷰 개수',
    AVG(star) AS '별점 평균값'
    FROM review AS r INNER JOIN item AS i ON r.item_id = i.id
    INNER JOIN member AS m ON r.mem_id = m.id    
    WHERE i.gender = 'u'
    GROUP BY YEAR(i.registration_date)
    HAVING COUNT(*) >= 10
    ORDER BY AVG(star) DESC;
    