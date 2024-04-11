
SELECT subreddit, title, author, score,
  CASE
    WHEN score BETWEEN 15000 AND 20000 THEN 'Perfect'
    WHEN score BETWEEN 10000 AND 15000 THEN 'Good'
    WHEN score BETWEEN 5000 AND 10000 THEN 'Not Bad'
    WHEN score BETWEEN 1000 AND 5000 THEN 'Bad'
    ELSE 'Out of the Way'
  END AS "interest"
FROM "Reddit"
WHERE score > (SELECT AVG(score) AS AverageScore FROM "Reddit")
ORDER BY score DESC;

SELECT * FROM "Reddit";


SELECT * FROM "Reddit"
ORDER by score DESC 
LIMIT 10;



SELECT * FROM "Reddit"
ORDER by comments_number DESC 
LIMIT 10;



SELECT author, title, time,
  CASE
    WHEN strftime('%H', datetime(time)) BETWEEN '00' AND '08' THEN 'morning'
    WHEN strftime('%H', datetime(time)) BETWEEN '08' AND '16' THEN 'afternoon'
    WHEN strftime('%H', datetime(time)) BETWEEN '16' AND '24' THEN 'night'
    ELSE NULL
  END as "GoldenTime"
FROM "Reddit";


SELECT author ,COUNT(author) AS "Number_of_author"
FROM "Reddit"
GROUP BY author;


SELECT author ,COUNT(author) AS "Number_of_author"
FROM "Reddit"
WHERE score > 1000
GROUP BY author;


SELECT subreddit, title, author, score,
  CASE
    WHEN score BETWEEN 15000 AND 20000 THEN 'Perfect'
    WHEN score BETWEEN 10000 AND 15000 THEN 'Good'
    WHEN score BETWEEN 5000 AND 10000 THEN 'Not Bad'
    WHEN score BETWEEN 1000 AND 5000 THEN 'Bad'
    ELSE 'Out of the Way'
  END AS "interest"
FROM "Reddit"
WHERE score > (SELECT AVG(score) AS AverageScore FROM "Reddit")
ORDER BY score DESC;




