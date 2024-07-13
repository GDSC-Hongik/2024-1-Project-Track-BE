SELECT p.name , COALESCE(s.sales_volume, '판매량 정보 없음') AS '판매량' 
FROM pizza_price_cost AS p LEFT OUTER JOIN sales AS s ON p.id = s.menu_id;