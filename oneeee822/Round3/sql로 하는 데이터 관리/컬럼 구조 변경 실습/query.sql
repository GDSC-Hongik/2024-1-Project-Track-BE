# 여기에 코드를 작성하세요
ALTER TABLE shoes RENAME COLUMN name TO model;
ALTER TABLE shoes MODIFY size DOUBLE NOT NULL;
ALTER TABLE shoes DROP COLUMN brand;
ALTER TABLE shoes ADD stock INT NOT NULL;



# 테스트 코드
DESCRIBE shoes;