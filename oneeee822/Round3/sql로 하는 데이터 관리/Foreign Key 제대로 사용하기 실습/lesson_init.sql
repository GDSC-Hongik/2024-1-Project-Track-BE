CREATE TABLE customer_order (
id INT NOT NULL AUTO_INCREMENT,
item_no INT NOT NULL,
payment_id INT NOT NULL,
approval_time DATETIME NOT NULL,
PRIMARY KEY(id));
    
CREATE TABLE delivery (
id INT NOT NULL AUTO_INCREMENT,
order_id INT NULL,
location_code TINYINT NOT NULL,
status_code TINYINT NOT NULL,
recent_update_time DATETIME NOT NULL,
PRIMARY KEY(id));
    
INSERT INTO customer_order VALUES (10000, 102, 1304, '2020-06-02 17:42:29');    
INSERT INTO customer_order VALUES (10001, 304, 1305, '2020-06-02 17;50:04'); 
INSERT INTO customer_order VALUES (10002, 2091, 1306, '2020-06-02 18:00:51');


INSERT INTO delivery VALUES (9983, 10000, 1, 0, '2020-06-03 18:00:23');
INSERT INTO delivery VALUES (9984, 10001, 3, 1, '2020-06-04 15:23:27');
INSERT INTO delivery VALUES (9985, 10002, 4, 2, '2020-06-05 09:12:03');
