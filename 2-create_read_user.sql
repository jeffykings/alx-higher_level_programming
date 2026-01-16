--  a script that creates the database hbtn_0d_2 and the user user_0d_2.

-- user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
-- The user_0d_2 password should be set to user_0d_2_pwd
-- If the database hbtn_0d_2 already exists, your script should not fail
-- If the user user_0d_2 already exists, your script should not fail


-- Create database and doesn't fail if already exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user na doesnt fail if already exists
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';

-- Grant only SELECT privilege on the database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';


-- APPLY CHANGES
FLUSH PRIVILEGES;
