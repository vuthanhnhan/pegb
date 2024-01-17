CREATE TABLE tier (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50),
    min_orders INT,
    max_orders INT,
    discount INT NULL
);

INSERT INTO tier (category_name, min_orders, max_orders, discount) VALUES
    ('Bronze', 0, 20, 10),
    ('Silver', 21, 49, 20),
    ('Gold', 50, NULL, 30);
