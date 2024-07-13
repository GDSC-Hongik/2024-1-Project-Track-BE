CREATE TABLE `employee` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` text,
  `age` int DEFAULT NULL,
  `department` text,
  `address` text,
  `phone_num` text,
  `hire_date` date,
  `rating_grade` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `employee` (`id`, `name`, `age`, `department`, `address`, `phone_num`, `hire_date`, `rating_grade`)
VALUES 
(1, '김승희', 28, '인사팀', '서울특별시 용산구 한남대고 52 207호', '010-7208-9011', '2017-04-13', 'B+'),
(2, '강민수', 32, '인사팀', '서울특별시 성동구 서울숲2길 32-13 301호', '010-3453-2019', '2018-11-25', 'A-'),
(3, '이나연', 28, '개발팀', '경기도 김포시 걸포동 43 102호', '010-3567-2312', '2020-01-04', 'B-'),
(4, '구혜림', 33, '개발팀', '서울특별시 용산구 한남대고 해피하우스 207호', '010-2139-5768', '2019-02-05', 'A+'),
(5, '백두민', 27, '개발팀', '경기도 성남시 수정구 신흥동 우와아파트 1101호', '010-7733-4532', '2018-09-12', 'A-'),
(6, '최민준', 28, '홍보팀', '경기도 고양시 일산서구 탄현동 현미아파트 604호', '010-8577-9280', '2018-03-26', 'B-'),
(7, '하태림', 26, '홍보팀', '인천시 연수구 송도동 레이스아파트 1102호', '010-3469-0912', '2018-09-21', 'C');
