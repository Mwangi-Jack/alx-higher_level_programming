-- This script;
-- creates a database 'hbtn_0d_2
-- creates user 'user_0d_2'
-- 'user_0d_2 is given SELECT PRIVILEGE
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT  ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
