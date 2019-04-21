CREATE TABLE Roads (
    road_id     SERIAL PRIMARY KEY,
    name        VARCHAR(80) NOT NULL
);

CREATE TABLE Typess (
    type_id             SERIAL PRIMARY KEY,
    weight              INTEGER     NOT NULL,
    road_id             INTEGER     NOT NULL,
    FOREIGN KEY (road_id)
    REFERENCES Roads (road_id)
);


INSERT INTO Roads (name) VALUES ('Tarmac'), ('Gravel'), ('Snow');

CREATE TABLE Bicycles (
    bicycle_id          SERIAL PRIMARY KEY,
    brand               VARCHAR(80) NOT NULL,
    model               VARCHAR(80) NOT NULL,
    road_legal          boolean     NOT NULL,
    type_id             INTEGER,
    FOREIGN KEY (type_id)
    REFERENCES Typess (type_id)
);




CREATE TABLE Owners (
    owner_id            SERIAL PRIMARY KEY,
    name                VARCHAR(80) NOT NULL UNIQUE,
    age                 INTEGER     NOT NULL,
    pro                 BOOLEAN     NOT NULL,
    bicycle_id          INTEGER,
    type_id             INTEGER,
    FOREIGN KEY (bicycle_id)
    REFERENCES Bicycles (bicycle_id)
    ON DELETE SET NULL,
    FOREIGN KEY (type_id)
    REFERENCES Typess (type_id)
);
