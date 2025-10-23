-- Liste le nombre d'enregistrements pour chaque score dans second_table
SELECT score, COUNT(score) AS number 
FROM second_table 
GROUP BY score 
ORDER BY number DESC;
