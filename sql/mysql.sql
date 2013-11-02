// Counting rows in each table of DB
SELECT table_name, table_rows
    FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_SCHEMA = '<database_name>';
