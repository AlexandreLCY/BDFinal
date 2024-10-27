/* Lógico_1: */

CREATE TABLE Filme (
    IDfilme INT PRIMARY KEY,
    Sinopse CHAR(255),
    Titulo CHAR(50),
    Link CHAR(100),
    Avaliacao FLOAT,
    Duracao FLOAT
);

CREATE TABLE Usuario (
    ID_user INT PRIMARY KEY,
    Username CHAR(30)
);

CREATE TABLE Direcao (
    Nome CHAR(150),
    ID INT PRIMARY KEY
);

CREATE TABLE Genero (
    id INT PRIMARY KEY,
    Genero CHAR(30)
);

CREATE TABLE Avalia (
    fk_Usuario_ID_user INT,
    fk_Filme_IDfilme INT,
    Nota FLOAT,
    DataHora DATE
);

CREATE TABLE tem (
    fk_Genero_id INT,
    fk_Filme_IDfilme INT
);

CREATE TABLE produzido (
    fk_Direcao_ID INT,
    fk_Filme_IDfilme INT,
    DataLancamento DATE PRIMARY KEY
);
 
ALTER TABLE Avalia ADD CONSTRAINT FK_Avalia_1
    FOREIGN KEY (fk_Usuario_ID_user)
    REFERENCES Usuario (ID_user)
    ON DELETE SET NULL;
 
ALTER TABLE Avalia ADD CONSTRAINT FK_Avalia_2
    FOREIGN KEY (fk_Filme_IDfilme)
    REFERENCES Filme (IDfilme)
    ON DELETE SET NULL;
 
ALTER TABLE tem ADD CONSTRAINT FK_tem_1
    FOREIGN KEY (fk_Genero_id)
    REFERENCES Genero (id)
    ON DELETE RESTRICT;
 
ALTER TABLE tem ADD CONSTRAINT FK_tem_2
    FOREIGN KEY (fk_Filme_IDfilme)
    REFERENCES Filme (IDfilme)
    ON DELETE SET NULL;
 
ALTER TABLE produzido ADD CONSTRAINT FK_produzido_2
    FOREIGN KEY (fk_Direcao_ID)
    REFERENCES Direcao (ID)
    ON DELETE RESTRICT;
 
ALTER TABLE produzido ADD CONSTRAINT FK_produzido_3
    FOREIGN KEY (fk_Filme_IDfilme)
    REFERENCES Filme (IDfilme)
    ON DELETE RESTRICT;