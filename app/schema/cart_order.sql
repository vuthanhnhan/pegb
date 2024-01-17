CREATE TABLE cart_order (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    status ENUM('pending', 'complete') NOT NULL DEFAULT 'pending',
    total_amount DECIMAL(10, 2),
    FOREIGN KEY (user_id) REFERENCES user(id)
);
