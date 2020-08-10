-- creates the database hbtn_0c_0 in your MySQL server
-- sql script
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE hbnb_dev_db
CREATE USER IF NOT EXISTS hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db TO hbnb_dev@localhost;
GRANT SELECT ON performance_schema TO hbnb_dev@localhost;
SET PASSWORD FOR hbnb_dev@localhost = 'hbnb_dev_pwd';
