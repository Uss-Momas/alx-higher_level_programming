-- creating DB and table
-- create DB
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

-- create table
CREATE TABLE IF NOT EXISTS cities(
  id INT PRIMARY KEY AUTO_INCREMENT,
  state_id INT,
  name VARCHAR(256) NOT NULL,
  FOREIGN KEY(state_id) REFERENCES states(id)
);
