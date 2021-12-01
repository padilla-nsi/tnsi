-- SQLite
.open "MEDIATHEQUE";

CREATE TABLE "LIVRE" (
  "isbn" VARCHAR(42),
  "titre" VARCHAR(42),
  "editeur" VARCHAR(42),
  "annee" VARCHAR(42),
  PRIMARY KEY ("isbn")
);

CREATE TABLE "EMPRUNTE" (
  "code_barre" VARCHAR(42),
  "isbn" VARCHAR(42),
  PRIMARY KEY ("code_barre", "isbn"),
  FOREIGN KEY ("code_barre") REFERENCES "USAGER" ("code_barre"),
  FOREIGN KEY ("isbn") REFERENCES "LIVRE" ("isbn")
);

CREATE TABLE "USAGER" (
  "code_barre" VARCHAR(42),
  "nom" VARCHAR(42),
  "prenom" VARCHAR(42),
  "adresse" VARCHAR(42),
  "cp" VARCHAR(42),
  "ville" VARCHAR(42),
  "email" VARCHAR(42),
  PRIMARY KEY ("code_barre")
);

CREATE TABLE "ECRIT_PAR" (
  "a_id" VARCHAR(42),
  "isbn" VARCHAR(42),
  PRIMARY KEY ("a_id", "isbn"),
  FOREIGN KEY ("a_id") REFERENCES "AUTEUR" ("a_id"),
  FOREIGN KEY ("isbn") REFERENCES "LIVRE" ("isbn")
);

CREATE TABLE "AUTEUR" (
  "a_id" VARCHAR(42),
  "nom" VARCHAR(42),
  "prenom" VARCHAR(42),
  PRIMARY KEY ("a_id")
);