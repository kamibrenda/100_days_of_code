--Write a select statement that takes name from person table and return "Hello, <name> how are you doing today?" results in a column named greeting
SELECT 
    'Hello, ' || name || ' how are you doing today?' AS greeting
FROM
    person;

