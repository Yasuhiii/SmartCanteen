CREATE DATABASE smartcanteen;
USE smartcanteen;

CREATE TABLE utilizador (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo ENUM('estudante','funcionario') NOT NULL,
    nome VARCHAR(100) NOT NULL,
    numero VARCHAR(20) UNIQUE NOT NULL,
    curso_departamento VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    saldo DECIMAL(10,2) DEFAULT 0,
    password VARCHAR(255)
);

CREATE TABLE refeicao (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    categoria VARCHAR(50),
    preco DECIMAL(6,2),
    quantidade_diaria INT
);

CREATE TABLE carregamento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_utilizador INT,
    valor DECIMAL(10,2),
    data DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_utilizador) REFERENCES utilizador(id)
);

CREATE TABLE compra (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_utilizador INT,
    id_refeicao INT,
    quantidade INT,
    data DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_utilizador) REFERENCES utilizador(id),
    FOREIGN KEY (id_refeicao) REFERENCES refeicao(id)
);