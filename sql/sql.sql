CREATE DATABASE IF NOT EXISTS db_municipios;
USE db_municipios;

DROP TABLE IF EXISTS estados;
DROP TABLE IF EXISTS municipios;

CREATE TABLE estados (
    id int primary key,
    nome varchar(50) not null,
    sigla char(2) not null unique,
) ENGINE=INNODB;

CREATE TABLE municipios (
    id int auto_increment primary key,
    nome varchar(100) not null,
    id_estado int not null,
    foreign key(id_estado) 
    references estados(id)
    on delete cascade,
) ENGINE=INNODB;