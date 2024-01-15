-- write a function that takes an argument and returns the square of it.
-- you are given a table 'square' with column 'n'
-- return a table with:
--   this column and your result in a column named 'res'

SELECT n, CAST(POWER(n, 2) AS integer) AS res
FROM  square;