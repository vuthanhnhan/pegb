# PEGB E-commerce

Brief project description and purpose.

## Table of Contents

- [Deployment Instructions](#deployment-instructions)
- [Release Notes](#release-notes)

## Deployment Instructions

### Prerequisites

- Docker and Docker Compose installed on the deployment machine.

### Deployment Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/vuthanhnhan/pegb
   cd pegb
   docker-compose up

# Release Notes

## Date: 2023-17-01

### Overview

This release introduces several new features, aimed at improving the overall functionality and user experience of Pinchi Inc's e-commerce system.

### New Features

1. **Customer Categorization:**
   - Introduction of customer categorization based on the number of successful orders.
   - Bronze: 0-20 orders
   - Silver: 21-49 orders
   - Gold: 50 and above orders

2. **Discounts:**
   - Periodic discounts on selected products based on the combination of customer category and product category.
   - Discount values are maintained as a percentage.

3. **Shopping Cart:**
   - Enhanced shopping cart functionality for both registered and unregistered customers.
   - Customers can view products, add items to the cart, and remove items from the cart.

### Enhancements

1. **Product Management:**
   - Staff can now perform create, update, and delete operations on products within their assigned department.

2. **User Onboarding:**
   - Improved self-registration process for customers with a verification email sent upon registration.

3. **Order History:**
   - Registered customers can now fetch their order history, providing a comprehensive view of their past purchases.

### Configuring Environment File

To ensure a seamless deployment of the latest version, make sure to update your environment configuration. Follow the steps below:

1. Open the `.env` file in app folder.
2. Update the following key-value pairs based on your deployment environment:

   ```env
   MYSQL_HOST=your_mysql_host
   MYSQL_USER=your_mysql_user
   MYSQL_PASSWORD=your_mysql_password
   MYSQL_DATABASE=your_mysql_database
   SECRET_KEY=your_secret_key

4. Open the `.env` file in frontend folder.
5. Update the following key-value pairs based on your deployment environment:

   ```env
   VUE_APP_BACKEND_URL=your_backend_url

### Demonstration Video

For a visual walkthrough of the new features and enhancements introduced in this release, I have prepared a demonstration video.

[Watch the Demonstration Video](https://youtu.be/IT_t5VhK6Jw)

### Contributors

   - Vu Thanh Nhan
