CREATE TABLE vendas_carros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    marca VARCHAR(50),
    modelo VARCHAR(50),
    ano INT,
    preco DECIMAL(10,2),
    data_venda DATE,
    vendedor VARCHAR(50),
    regiao VARCHAR(50)
);

INSERT INTO vendas_carros (marca, modelo, ano, preco, data_venda, vendedor, regiao) VALUES
('Toyota', 'Corolla', 2020, 95000, '2024-01-10', 'João', 'Sudeste'),
('Honda', 'Civic', 2019, 90000, '2024-01-15', 'Maria', 'Sul'),
('Ford', 'Focus', 2018, 70000, '2024-02-01', 'Carlos', 'Nordeste'),
('Chevrolet', 'Onix', 2022, 85000, '2024-02-10', 'Ana', 'Sudeste'),
('Hyundai', 'HB20', 2021, 80000, '2024-03-05', 'Pedro', 'Centro-Oeste');