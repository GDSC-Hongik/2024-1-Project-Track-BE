# 여기에 코드를 작성하세요
CREATE TABLE beta_review_20s LIKE beta_review;
INSERT INTO beta_review_20s SELECT * FROM beta_review WHERE age>=20 AND age <30;

# 테스트 코드
SELECT * FROM beta_review_20s;