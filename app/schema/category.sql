CREATE TABLE category (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES department(id)
);

INSERT INTO category (name, department_id) VALUES
    ('Frozen Foods', 1),
    ('Fresh Produce', 1),
    ('Electronics Accessories', 2),
    ('Men''s Apparel', 3),
    ('Women''s Apparel', 3);
