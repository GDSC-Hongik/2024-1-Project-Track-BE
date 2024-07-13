CREATE TABLE item (
id INT NOT NULL AUTO_INCREMENT,
name VARCHAR(20) NOT NULL,
type VARCHAR(20) NOT NULL,
price INT NOT NULL,
description VARCHAR(200) NOT NULL,
upload_date DATE NOT NULL,
purchased CHAR(1) NOT NULL,
is_deleted CHAR(1) NOT NULL,
PRIMARY KEY(id));

INSERT INTO item (name, type, price, description, upload_date, purchased, is_deleted) VALUES ('신생아 모자', '의류', 20000, '굵은 망사형 제품으로..', '2019-03-23', 'N', 'Y');

INSERT INTO item (name, type, price, description, upload_date, purchased, is_deleted) VALUES ('아이팻 프로', '전자기기', 300000, '작동하는데는 큰 문제 없어요, 대신..', '2020-01-05', 'Y', 'Y');

INSERT INTO item (name, type, price, description, upload_date, purchased, is_deleted) VALUES ('남성정장 상하의 세트', '의류', 100000, '제가 보통 상의가 100이고, 하의를..', '2018-07-03', 'N', 'N');

INSERT INTO item (name, type, price, description, upload_date, purchased, is_deleted) VALUES ('나무로 된 수납장', '가구/인테리어', 50000, '꽤 좋은 원목으로 만들어진..', '2020-05-23', 'Y', 'N');

INSERT INTO item (name, type, price, description, upload_date, purchased, is_deleted) VALUES ('Java 관련 책들', '도서', 50000, '자바 공부 엄청 열심히 한 시절에..', '2020-04-17', 'N', 'Y');

INSERT INTO item (name, type, price, description, upload_date, purchased, is_deleted) VALUES ('대학생용 백팩', '악세서리', 800000, '명품 브랜드 XXX 거에요, 진짜 아끼는 건데..', '2017-02-05', 'Y', 'Y');

INSERT INTO item (name, type, price, description, upload_date, purchased, is_deleted) VALUES ('나이끼 조던 한정판', '의류', 1200000, '선물로 같은 종류의 한정판 신발을..', '2018-10-06', 'N', 'Y');