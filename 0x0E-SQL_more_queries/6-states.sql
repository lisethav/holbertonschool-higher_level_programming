-- creates the database hbtn_0d_usa and the table states
CREATE DATABASE if not exists hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE table if not exists states (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256) NOT NULL);
