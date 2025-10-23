-- Liste tous les enregistrements de second_table où name n'est pas NULL
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
