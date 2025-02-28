-- Creates a table named 'users' with the following attributes:
-- id: integer, never null, auto increment, primary key
-- email: string (255 characters), never null, unique
-- name: string (255 characters)
-- If the table already exists, the script should not fail

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);