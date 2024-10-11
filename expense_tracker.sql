CREATE DATABASE expense_tracker;

USE expense_tracker;

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(255),
    amount DECIMAL(10, 2),
    date DATE,
    category VARCHAR(50),
    type ENUM('Income', 'Expense'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
