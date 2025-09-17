# Mysql

## 常用命令
How to see full query from SHOW PROCESSLIST?

https://stackoverflow.com/questions/3638689/how-to-see-full-query-from-show-processlist

```mysql
SHOW FULL PROCESSLIST;
SHOW processlist;
```

## How can I get the size of a MySQL database?
https://stackoverflow.com/questions/1733507/how-can-i-get-the-size-of-a-mysql-database

```mysql
SELECT table_schema "DB Name",
        ROUND(SUM(data_length + index_length) / 1024 / 1024, 1) "DB Size in MB"
FROM information_schema.tables
GROUP BY table_schema;
```

## show slave status
SHOW SLAVE STATUS\G

## mysql example
```sql
CREATE DATABASE sunyangjian_test
  DEFAULT CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE sunyangjian_test;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO users (username, email, password_hash)
VALUES ('john_doe', 'john@example.com', 'hashed_password_123');

INSERT INTO users (username, email, password_hash)
VALUES ('alice_wonder', 'alice@example.com', '$2a$10$abcDEF123xyz789...');
```