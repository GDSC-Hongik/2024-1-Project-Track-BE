CREATE TABLE shoes (
id INT NOT NULL AUTO_INCREMENT,
name VARCHAR(10) NOT NULL,
size INT NOT NULL,
brand VARCHAR(20) NULL,
PRIMARY KEY(id)
);

INSERT INTO shoes (name, size, brand) VALUES ('MK-120', 260, 'Nice');
INSERT INTO shoes (name, size, brand) VALUES ('AOS-347', 270, 'Akidas');
INSERT INTO shoes (name, size, brand) VALUES ('ZMQ-83', 260, 'Heebok');