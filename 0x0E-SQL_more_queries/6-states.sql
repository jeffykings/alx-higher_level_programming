-- Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.

-- states description:
-- id INT unique, auto generated, can’t be null and is a primary key
-- name VARCHAR(256) can’t be null
-- If the database hbtn_0d_usa already exists, your script should not fail
-- If the table states already exists, your script should not fail

-- create a database if doesn't exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- switch to the database
USE hbtn_0d_usa;

-- create a table for the database is it doesn't exist
CREATE TABLE IF NOT EXISTS states(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL);
