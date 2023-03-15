-- creating database and user
-- creating DB
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Creating user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED WITH auth_socket BY 'user_0d_2_pwd';
FLUSH PRIVILEGES;

-- granting privileges
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
