CREATE DATABASE IF NOT EXISTS air_quality;
USE air_quality;

CREATE TABLE IF NOT EXISTS air (
    id INT PRIMARY KEY AUTO_INCREMENT,
    date_01 DATE NOT NULL,
    pm2_5 INT CHECK (pm2_5 >= 0),
    no2 INT CHECK (no2 >= 0),
    so2 INT CHECK (so2 >= 0)
);
