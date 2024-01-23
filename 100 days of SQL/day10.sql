-- # write your SQL statement here: you are given a table 'ispalindrome' with column 'str', return a table with column 'str' and your result in a column named 'res'.
-- Assuming you have a table named 'ispalindrome' with a column 'str'
-- Return a table with column 'str' and a boolean result column named 'res'
SELECT str, 
       CASE WHEN LOWER(str) = LOWER(REVERSE(str)) THEN TRUE ELSE FALSE END as res
FROM ispalindrome;
