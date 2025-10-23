-- Liste toutes les villes de California en utilisant une sous-requête
SELECT id, name
FROM cities
WHERE state_id = 1
ORDER BY id ASC;
