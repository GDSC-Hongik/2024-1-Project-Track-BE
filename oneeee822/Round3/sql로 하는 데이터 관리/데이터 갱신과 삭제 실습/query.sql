# 여기에 코드를 작성하세요
UPDATE item SET is_deleted = 'Y' WHERE id = 3;
DELETE FROM item WHERE is_deleted ='Y' AND DATEDIFF('2020-07-05', upload_date)>365;




# 테스트 코드
SELECT * FROM item;