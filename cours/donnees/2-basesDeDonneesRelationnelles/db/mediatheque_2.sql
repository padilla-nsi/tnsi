-- configurer l'interprète SQLITE
pragma foreign_keys = true;


--Effacer les tables si la base n'est pas vierge
DROP TABLE IF EXISTS auteur_de;
DROP TABLE IF EXISTS auteur;
DROP TABLE IF EXISTS livre;
DROP TABLE IF EXISTS usager;
DROP TABLE IF EXISTS emprunt;

--01 - Recopier

CREATE TABLE livre (titre TEXT,
                    editeur TEXT,
                    annee INTEGER,
                    isbn TEXT PRIMARY KEY);

INSERT INTO livre VALUES ('Les Aventures de Huckleberry Finn', 'Flammarion', 2020, '978-2081509511');   
    
INSERT INTO livre (isbn, annee, titre, editeur) 
VALUES ('978-2207249123', 1999, 'Fondation et Empire', 'Editions Denoël');

INSERT INTO livre(titre, editeur, isbn) VALUES ('Akira', 'Glénat', '978-2723428262');

INSERT INTO livre(titre, annee, isbn) VALUES ('Les Robots', 2017, '978-2745989857');

INSERT INTO livre VALUES 
    ('Astérix chez les Pictes', 'Editions Albert René', '2013', '978-2864972662'),
    ('Les Monades urbaines', 'Robert Laffont', '2016', '978-2221197691'),
    ('Les Voyages de Gulliver', 'Primento', '2015', '978-2335008586'),
    ('Lolita', 'Penguin UK', '2012', '978-0141391601'),
    ('La Nuit des temps', 'Presses de la Cité', '2014', '978-2258116429');

SELECT * FROM livre;


--02 - Appliquer

CREATE TABLE auteur (a_id INTEGER PRIMARY KEY,
                     nom TEXT,
                     prenom TEXT);

INSERT INTO auteur VALUES
    (0, 'Twain', 'Mark'),
    (1, 'Asimov', 'Isaac'),
    (2, 'Ōtomo', 'Katsuhiro'),
    (3, 'Martelle', 'Myriam'),
    (4, 'Touache', 'Sébastien'),
    (5, 'Goscinny', 'René'),
    (6, 'Ferri', 'Jean-Yves'),
    (7, 'Uderzo', 'Albert'),
    (8, 'Conrad', 'Didier'),
    (9, 'SILVERBERG', 'Robert'),
    (10, 'Swift', 'Jonathan'),
    (11, 'Ligaran', ''),
    (12, 'Nabokov', 'Vladimir'),
    (13, 'BARJAVEL', 'René');

SELECT * FROM auteur;


--03 - Recopier - Clés primaires

DROP TABLE IF EXISTS auteur_de;

CREATE TABLE auteur_de (
    a_id    INTEGER,
    isbn    TEXT,
    FOREIGN KEY(a_id) REFERENCES auteur(a_id),  
    FOREIGN KEY(isbn) REFERENCES livre(isbn),
    PRIMARY KEY(a_id, isbn)
);

INSERT INTO auteur_de VALUES(0, '978-2081509511');

INSERT INTO auteur_de VALUES 
    (1, '978-2207249123'),
    (2, '978-2723428262'),
    (3, '978-2745989857'),
    (4, '978-2745989857'),
    (5, '978-2864972662'),
    (6, '978-2864972662'),
    (7, '978-2864972662'),
    (8, '978-2864972662'),
    (9, '978-2221197691'),
    (10, '978-2335008586'),
    (11, '978-2335008586'),
    (12, '978-0141391601'),
    (13, '978-2258116429');

SELECT * FROM auteur_de;

--erreur de clé unique car cette entité existe déjà
INSERT INTO auteur_de VALUES(0, '978-2081509511');

--erreur de clé étrangère -1000 n'existe pas...
INSERT INTO auteur_de VALUES (1000, '978-2864972662');

-- erreur : contrainte d'entité (clé étrangère)
INSERT INTO auteur_de VALUES (0, '123-1234567890');


--04 - Application

CREATE TABLE usager (
    code_barre TEXT PRIMARY KEY,
    nom TEXT,
    prenom TEXT,
    adresse TEXT,
    cp TEXT,
    ville TEXT,
    email TEXT);

CREATE TABLE emprunt (
    code_barre TEXT,
    isbn TEXT,
    FOREIGN KEY(code_barre) REFERENCES usager(code_barre),
    FOREIGN KEY(isbn) REFERENCES livre(isbn),
    PRIMARY KEY(code_barre, isbn)
);

--essais avec insertions de données fictives
INSERT INTO usager VALUES
    (123, 'padilla', 'pascal', '33 abbé de l''épée', '13005', 'marseille', 'liste2@mail.me');







