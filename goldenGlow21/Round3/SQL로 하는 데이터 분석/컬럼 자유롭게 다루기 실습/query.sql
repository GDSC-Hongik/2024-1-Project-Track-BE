SELECT name,
       price,
       price/cost,
       (CASE 
            WHEN price/cost >= 1 AND price/cost < 1.5 THEN 'C. 저효율 메뉴'
            WHEN price/cost >= 1.5 AND price/cost < 1.7 THEN 'B. 중효율 메뉴'
            WHEN price/cost >= 1.7 THEN 'A. 고효율 메뉴'
        END) AS efficiency
FROM pizza_price_cost
ORDER BY efficiency DESC, price ASC
LIMIT 6;
