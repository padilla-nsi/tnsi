-- option utile pour utiliser
-- sqlite3 et dbeaver
pragma foreign_keys = true;



CREATE TABLE client (
  idclient INTEGER,
  nom VARCHAR(50),
  prenom VARCHAR(50),
  email VARCHAR(50),
  PRIMARY KEY (idclient)
);

CREATE TABLE commande (
  idcmd INTEGER,
  idclient INTEGER,
  date DATE,
  adresselivraison VARCHAR(90),
  paiementvalide BOOLEAN,
  livraisonfaite BOOLEAN,
  PRIMARY KEY (idcmd),
  FOREIGN KEY (idclient) REFERENCES client(idclient)
);

CREATE TABLE article_commande (
  idcmd INTEGER,
  idarticle INTEGER,
  quantite INTEGER,
  PRIMARY KEY (idcmd, idarticle),
  FOREIGN KEY (idcmd) REFERENCES commande(idcmd),
  FOREIGN KEY (idarticle) REFERENCES article(idarticle)
);

CREATE TABLE article (
  idarticle INTEGER,
  libelle VARCHAR(50),
  description VARCHAR(90),
  prixencentimes INTEGER,
  PRIMARY KEY (idarticle)
);