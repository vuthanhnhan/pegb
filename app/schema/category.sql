CREATE TABLE category (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    image VARCHAR(255),
    department_id INT,
    discount INT NULL,
    FOREIGN KEY (department_id) REFERENCES department(id)
);

INSERT INTO category (name, image, discount, department_id) VALUES
    ('Frozen Foods', 'https://gubbagroup.com/wp-content/uploads/2020/02/Frozen-food.jpg', 30, 1),
    ('Fresh Produce', 'https://cdn.agriland.ie/uploads/2014/03/shutterstock_112976938-1.jpg', 30, 1),
    ('Electronics Accessories', 'https://royalstore.ae/storage/app/public/uploads/categories/mobile-accessories_1654176486.png', 30, 2),
    ('Men Clothes', 'https://www.instyle.com/thmb/EMeMmp7gV5ZC-QgM9f-7R_iLSr0=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/gettyimages-539573922-2000-a03885527cf14bb9b1719a5812fb1d26.jpg', 30, 3),
    ('Women Clothes', 'https://www.shutterstock.com/image-photo/beautiful-colorful-clothes-flying-isolatedwomens-600nw-2257875171.jpg', 30, 3);
