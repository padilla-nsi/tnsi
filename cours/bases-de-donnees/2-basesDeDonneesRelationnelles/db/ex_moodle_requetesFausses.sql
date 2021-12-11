-- option utile pour utiliser
-- sqlite3 et dbeaver
pragma foreign_keys = true;


DROP TABLE commande;
DROP TABLE client;
DROP TABLE produit;


CREATE TABLE client
    (cid INT PRIMARY KEY,
    nom VARCHAR(100),
    prenom VARCHAR(100),
    points_fidelite INT NOT NULL,
    CHECK (points_fidelite >= 0));
    

--2


CREATE TABLE client (cid INT PRIMARY KEY,
                     nom VARCHAR(100),
                     prenom VARCHAR(100),
                     points_fidelite INT NOT NULL,
                     CHECK (points_fidelite >= 0));
                 
CREATE TABLE commande (cid INT REFERENCES client(cid),
                       pid INT REFERENCES produit(pid),
                       date DATE NOT NULL);
                   
CREATE TABLE produit (pid INT PRIMARY KEY,
                      nom VARCHAR (100),
                      prix DECIMAL(10,2));
                  

-- 3

CREATE TABLE client (cid INT PRIMARY KEY,
                     nom VARCHAR(100),
                     prenom VARCHAR(100),
                     points_fidelite INT NOT NULL,
                     CHECK (points_fidelite >= 0));
                   
CREATE TABLE produit (pid INT PRIMARY KEY,
                      nom VARCHAR (100),
                      prix DECIMAL(10,2));
                 
CREATE TABLE commande (cid INT REFERENCES client(cid),
                       nom VARCHAR(100) REFERENCES produit(nom),
                       date DATE NOT NULL);
    
--4

CREATE TABLE client (cid INT PRIMARY KEY,
                     nom VARCHAR(100),
                     prenom VARCHAR(100),
                     points_fidelite INT NOT NULL,
                     CHECK (points_fidelite >= 0));
                   
CREATE TABLE produit (pid INT PRIMARY KEY,
                      nom VARCHAR (100),
                      prix DECIMAL(10,2));
                 
CREATE TABLE commande (cid INT REFERENCES client(cid),
                       pid INT REFERENCES produit(pid),
                       date DATE NOT NULL);
    
INSERT INTO commande VALUES (0, 0, '2021-03-02');                   

    