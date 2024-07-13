SELECT * 
FROM review 
WHERE item_id IN 
     (
      SELECT id 
      FROM item 
      WHERE registration_date < '2018-12-31'
     );
