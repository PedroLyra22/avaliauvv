CREATE DATABASE notalise;
USE notalise;

CREATE TABLE admin_user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    login VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE
);

CREATE TABLE evento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    data_inicial DATE NOT NULL,
    data_final DATE NOT NULL,
    imagem TEXT,
    descricao TEXT NOT NULL,
    cep VARCHAR(10) NOT NULL,
    rua VARCHAR(255) NOT NULL,
    bairro VARCHAR(100) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    numero VARCHAR(10) NOT NULL,
    complemento VARCHAR(80),
    admin_user_id INT,
    FOREIGN KEY (admin_user_id) REFERENCES admin_user(id)
);

CREATE TABLE estande (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    tema VARCHAR(255) NOT NULL,
    imagem LONGBLOB,
    descricao TEXT NOT NULL,
    evento_id INT,
    admin_user_id INT,
    FOREIGN KEY (evento_id) REFERENCES evento(id),
    FOREIGN KEY (admin_user_id) REFERENCES admin_user(id)
);

CREATE TABLE avaliacao_evento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nota_equipe TINYINT CHECK (nota_equipe BETWEEN 0 AND 5),
    nota_infraestrutura TINYINT CHECK (nota_infraestrutura BETWEEN 0 AND 5),
    nota_organizacao TINYINT CHECK (nota_organizacao BETWEEN 0 AND 5),
    nota_experiencia TINYINT CHECK (nota_experiencia BETWEEN 0 AND 5),
    imagem_avaliacao TEXT,
    evento_id INT,
    FOREIGN KEY (evento_id) REFERENCES evento(id)
);

CREATE TABLE avaliacao_estande (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nota_apresentacao TINYINT CHECK (nota_apresentacao BETWEEN 0 AND 5),
    nota_ideia TINYINT CHECK (nota_ideia BETWEEN 0 AND 5),
    nota_experiencia TINYINT CHECK (nota_experiencia BETWEEN 0 AND 5),
    imagem_avaliacao TEXT,
    estande_id INT,
    FOREIGN KEY (estande_id) REFERENCES estande(id)
);