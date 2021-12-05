-- configurer l'interprète SQLITE
pragma foreign_keys = true;


DROP TABLE IF EXISTS annuaire;

CREATE TABLE annuaire (
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    tel VARCHAR(20) NOT NULL UNIQUE PRIMARY KEY
);

INSERT INTO annuaire(nom, prenom, tel)  VALUES
    ('merveille', 'alice', '+33612345678'),
    ('breton', 'basile', '0609876543');
    
    
SELECT * FROM annuaire ;
