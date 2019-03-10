CREATE TABLE Bicycles (
  bicycle_id          SERIAL PRIMARY KEY,
  brand               VARCHAR(80) NOT NULL,
  model               VARCHAR(80) NOT NULL,
  road_legal          boolean     NOT NULL,
  weight              INTEGER     NOT NULL,
  type_id             INTEGER     NOT NULL,
  FOREIGN KEY (type_id)
  REFERENCES Typess (type_id)
);


CREATE TABLE Typess (
  type_id             SERIAL PRIMARY KEY,
  type_road           VARCHAR(80) NOT NULL,
  weight_class        VARCHAR(80) NOT NULL
);


CREATE TABLE Owners (
  owner_id            SERIAL PRIMARY KEY,
  name                VARCHAR(80) NOT NULL UNIQUE,
  age                 INTEGER     NOT NULL,
  pro                 BOOLEAN     NOT NULL,
  bicycle_id          INTEGER,
  type_id             INTEGER     NOT NULL,
  FOREIGN KEY (bicycle_id)
  REFERENCES Bicycles (bicycle_id)
  ON DELETE SET NULL,
  FOREIGN KEY (type_id)
  REFERENCES Typess (type_id)
);
