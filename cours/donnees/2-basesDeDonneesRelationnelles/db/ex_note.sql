-- option utile pour utiliser
-- sqlite3 et dbeaver
pragma foreign_keys = true;

CREATE TABLE eleve (
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    num VARCHAR(20) PRIMARY KEY
) ;

CREATE TABLE matiere (
    intitule VARCHAR(100) NOT NULL,
    mat_id INTEGER PRIMARY KEY
);

CREATE TABLE note (
    num_eleve VARCHAR(20) REFERENCES eleve(num),
    mat_id INT REFERENCES matiere(mat_id),
    note DECIMAL(4,2) NOT NULL,
    PRIMARY KEY (num_eleve, mat_id),
    CHECK (note >= 0 AND note <= 20)
);

INSERT INTO eleve VALUES 
    ('damier', 'alice', 1),
    ('elipse', 'basile', 2),
    ('figure', 'camille', 3);
    

INSERT  INTO matiere  VALUES
    ('NSI', 1),
    ('SES', 2),
    ('Maths', 3),
    ('SPC', 4);
    
INSERT INTO note VALUES
    (1, 1, 15),
    (2, 1, 6);