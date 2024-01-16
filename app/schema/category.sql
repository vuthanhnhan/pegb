CREATE TABLE category (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    department_id INT,
    discount INT NULL,
    FOREIGN KEY (department_id) REFERENCES department(id)
);

INSERT INTO category (name, department_id) VALUES
    ('Frozen Foods', 30, 1),
    ('Fresh Produce', 30, 1),
    ('Electronics Accessories', 30, 2),
    ('Men''s Apparel', 30, 3),
    ('Women''s Apparel', 30, 3);
