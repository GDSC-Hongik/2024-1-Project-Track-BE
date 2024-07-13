# 여기에 코드를 작성하세요
ALTER TABLE book 
    MODIFY isbn VARCHAR(50) NOT NULL UNIQUE,
    ADD CONSTRAINT page_rule CHECK (page>0),
    CHANGE kind genre_code INT NOT NULL,
    MODIFY location VARCHAR(10) NOT NULL DEFAULT 'warehouse';

# 테스트 코드
DESC book;