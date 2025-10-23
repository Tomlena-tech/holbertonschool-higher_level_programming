-- Crée la table unique_id avec id unique et valeur par défaut 1
CREATE TABLE IF NOT EXISTS uniq_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
