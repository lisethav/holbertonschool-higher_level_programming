-- creates the table unique_id on your MySQL server.
CREATE TABLE if not exists unique_id(id DEFAULT "1" UNIQUE, name VARCHAR(256));