CREATE DATABASE db;
CREATE table db.Prizes(
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    account_number VARCHAR(12) NOT NULL,
    prize VARCHAR(12) NOT NULL
);