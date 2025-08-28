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