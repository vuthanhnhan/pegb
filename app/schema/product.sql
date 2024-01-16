CREATE TABLE product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (category_id) REFERENCES category(id)
);

INSERT INTO product (category_id, name, price) VALUES
    (1, 'Frozen Pizza', 5.99),
    (2, 'Apples', 2.49),
    (3, 'USB Cable', 9.99),
    (4, 'Men''s T-Shirt', 19.99),
    (5, 'Women''s Jeans', 29.99);
