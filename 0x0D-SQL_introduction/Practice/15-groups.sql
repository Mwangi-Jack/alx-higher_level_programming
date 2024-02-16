-- script to list the number of records with the same score in
-- the table second_table
-- the result display the score and number of records for
-- this score with the lable number

SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC
