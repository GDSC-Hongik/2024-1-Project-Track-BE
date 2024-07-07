CREATE TABLE `member` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` text,
  `age` int DEFAULT NULL,
  `gender` text,
  `height` double DEFAULT NULL,
  `weight` double DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `sign_up_day` date DEFAULT NULL,
  `address` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `member` (`id`, `email`, `age`, `gender`, `height`, `weight`, `birthday`, `sign_up_day`, `address`) VALUES 
(1,'codeit@naver.com',28,'m',178.2,70,'1992-01-03','2019-03-26','서울특별시 중구 삼일대로 343 103호'),
(2,'korin02@google.com',29,'m',165.7,67.3,'1992-08-13','2019-02-27','서울특별시 중구 세종대로 110 502호'),
(3,'cowboy@codeit.kr',31,'m',NULL,70.2,'1990-01-03','2019-01-05','경기도 고양시 일산서구 고양대로 633 204동 203호'),
(4,'get_flower@naver.com',-10,'f',183.5,72,'1975-03-12','2018-11-29',NULL),
(5,'taehos@hanmail.net',27,'m',181.3,70,'1992-09-02','2017-03-14','제주 제주시 문연로 6 102동 1105호'),(6,'iamstylish@naver.com',300,'f',172.2,NULL,'1989-01-03','2012-11-15','안드로메다 128행성'),(7,'captainGoGo03@koreauniv.com',28,'m',195.2,66,'1992-03-13','2014-03-18','전라남도 순천시 왕지3길 60 112동 107호'),(8,'sungsos@naver.com',36,'f',167.7,66.2,'1992-01-03','2017-03-20','경기도 부천시 평천로 679 101동 101호'),(9,'young05@naver.com',30,'m',180.2,70.4,'1991-02-13','2013-08-12','경기 오산시 세마문학로 50 111동 109호'),(10,'codeman_to@yonseit.com',111,'f',NULL,70.5,'1970-08-01','2017-02-20','경기 고양시 덕양구 충장로 118 112동 1103호'),(11,'programmer007@sumsung.com',27,'m',170.4,65.3,'1993-03-26','2014-01-22','경기 성남시 수정구 시민로 209 101동 1201호'),(12,'lovely_day@kaisty.com',-10,'f',162.7,69.4,'1995-10-11','2017-07-01','경기 화성시 봉담읍 동화새터길 55-39 203동 205호'),(13,'teddy@kakaot.com',41,'f',177.3,77.2,'1980-11-12','2016-08-03','인천 부평구 아트센터로 118 302동 602호'),(14,'pooh_man@naver.com',28,'m',182,NULL,'1993-12-21','2018-09-02','인천 미추홀구 송림로 194 602동 303호'),(15,'bicycle_go123@yahoot.com',24,'m',180,60.3,'1997-03-03','2019-12-01','서울 송파구 올림픽로 435 103동 501호'),(16,'all_round321@naver.com',26,'m',182.4,NULL,'1995-01-03','2019-11-23',NULL),(17,'nice_man@google.com',200,'m',180.8,NULL,'2003-01-03','2015-10-25','강원도 원주시 가곡로 50 101동 810호'),(18,'jw101@hanmail.net',0,'m',160.3,70,'1992-08-03','2017-09-23','강원도 춘천시 지석로 29 402동 321호'),(19,'cat_movie@lotte.com',-5,'f',180.2,NULL,'1989-01-03','2018-11-25','서울 양천구 오목로 354 110동 402호'),(20,'gogo_shopping@naver.com',32,'m',180.2,80.3,'1989-11-02','2015-01-23','서울 송파구 올림픽로35길 10 파크리오 301동 703호'),(21,'hello_hat@unista.com',26,'f',165.3,48.2,'1995-11-13','2018-12-23',NULL),(22,'new_coder@naver.com',-2,'f',180.7,70,'1976-08-03','2018-12-12','부산 연제구 양연로27번길 26 301동 701호'),(23,'zerotohundred@naver.com',20,'m',162,56,'2001-02-17','2015-07-20',NULL),(24,'xMan_series@naver.com',29,'m',173,65,'1992-01-03','2011-12-20','어린왕자에 나오는 B612');