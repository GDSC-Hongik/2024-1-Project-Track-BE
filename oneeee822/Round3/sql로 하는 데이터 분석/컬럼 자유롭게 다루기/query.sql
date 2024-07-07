SELECT name, price, price/cost,
(CASE
    WHEN 1 <= price/cost AND price/cost < 1.5 THEN 'C. 저효율 메뉴'
    WHEN 1.5 <= price/cost AND price/cost < 1.7 THEN 'B. 중효율 메뉴'
    WHEN 1.7 <= price/cost  THEN 'A. 고효율 메뉴'
END) AS efficiency
FROM pizza_price_cost
ORDER BY efficiency DESC, price ASC LIMIT 6;
    