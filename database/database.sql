CREATE DATABASE gomarket;
USE gomarket;
CREATE TABLE IF NOT EXISTS producto(
	idProducto VARCHAR(10) PRIMARY KEY UNIQUE NOT NULL,
	nombre VARCHAR(80) NOT NULL,
    descripcion VARCHAR(500) NOT NULL,
    precio DECIMAL(10,0) NOT NULL,
    stock INT NOT NULL,
    imagen VARCHAR(150) NOT NULL
);