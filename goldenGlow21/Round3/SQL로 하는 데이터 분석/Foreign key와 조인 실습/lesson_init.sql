CREATE TABLE pizza_price_cost (id INTEGER PRIMARY KEY, name TEXT, price INTEGER, cost INTEGER);
INSERT INTO pizza_price_cost VALUES (1, 'Potato Bacon Pizza', 22000, 14000);
INSERT INTO pizza_price_cost VALUES (2, 'Sweet Potato Pizza', 24000, 14000);
INSERT INTO pizza_price_cost VALUES (3, 'Combination Pizza', 25000, 13000);
INSERT INTO pizza_price_cost VALUES (4, 'Bacon Cheddar Pizza', 32000, 20000);
INSERT INTO pizza_price_cost VALUES (5, 'Pineapple Pizza', 25000, 22000);
INSERT INTO pizza_price_cost VALUES (6, 'Garlic Shrimp Pizza', 26000, 19000);
INSERT INTO pizza_price_cost VALUES (7, 'Cheeze Pizza', 23000, 17000);
INSERT INTO pizza_price_cost VALUES (8, 'Pepperoni Pizza', 24000, 13000);

CREATE TABLE sales (id INTEGER PRIMARY KEY, menu_id INTEGER, sales_volume INTEGER);
INSERT INTO sales VALUES (1, 2, 220);
INSERT INTO sales VALUES (2, 3, 137);
INSERT INTO sales VALUES (3, 5, 121);
INSERT INTO sales VALUES (4, 6, 225);
INSERT INTO sales VALUES (5, 8, 167);