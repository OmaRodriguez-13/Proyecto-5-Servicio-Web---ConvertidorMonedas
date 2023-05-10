create database conversiones;
use conversiones;

CREATE TABLE `conversiones`.`tasas_cambio` (
  `moneda_origen` VARCHAR(40) NOT NULL,
  `moneda_destino` VARCHAR(40) NOT NULL,
  `tasa_cambio` FLOAT NOT NULL,
  PRIMARY KEY (`moneda_origen`, `moneda_destino`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;

INSERT INTO tasas_cambio (moneda_origen, moneda_destino, tasa_cambio) VALUES
/*DOLAR ESTADOUNIDENSE*/
('USD', 'EUR', 0.90425),
('USD', 'JPY', 132.49775),
('USD', 'CAD', 1.33282),
('USD', 'AUD', 1.33),
('USD', 'GBP', 0.79818),
('USD', 'MXN', 18.02190),
('USD', 'RUP', 81.70000),
('USD', 'CNY', 6.86950),
('USD', 'ARS', 214.67890),
/*EURO*/
('EUR', 'USD', 1.10608),
('EUR', 'GBP', 0.88260),
('EUR', 'AUD', 1.62970),
('EUR', 'CAD', 1.47419),
('EUR', 'JPY', 146.48440),
('EUR', 'MXN', 19.93903),
('EUR', 'RUP', 90.37253),
('EUR', 'CNY', 7.59824),
('EUR', 'ARS', 237.45062),
/*DOLAR CANADIENSE*/
('CAD', 'USD', 0.75034),
('CAD', 'EUR', 0.67834),
('CAD', 'GBP', 0.59870),
('CAD', 'JPY', 99.42039),
('CAD', 'AUD', 1.10551),
('CAD', 'MXN', 13.53305),
('CAD', 'RUP', 61.30314),
('CAD', 'CNY', 5.15404),
('CAD', 'ARS', 161.07726),
/*LIBRA ESTERLINA*/
('GBP', 'USD', 1.25328),
('GBP', 'EUR', 1.13296),
('GBP', 'CAD', 1.67028),
('GBP', 'JPY', 166.00069),
('GBP', 'AUD', 1.84610),
('GBP', 'MXN', 22.60393),
('GBP', 'RUP', 102.40804),
('GBP', 'CNY', 8.60992),
('GBP', 'ARS', 269.04356),
/*RUBLO RUSO*/
('RUP', 'USD', 0.01224),
('RUP', 'EUR', 0.01106),
('RUP', 'CAD', 0.0163),
('RUP', 'JPY', 1.62097),
('RUP', 'AUD', 0.01803),
('RUP', 'MXN', 0.22075),
('RUP', 'GBP', 0.00976),
('RUP', 'CNY', 0.08407),
('RUP', 'ARS', 2.62767),
/*PESO ARGENTINO*/
('ARS', 'USD', 0.00466),
('ARS', 'EUR', 0.00421),
('ARS', 'CAD', 0.00621),
('ARS', 'JPY', 0.61677),
('ARS', 'AUD', 0.00686),
('ARS', 'MXN', 0.08402),
('ARS', 'GBP', 0.00372),
('ARS', 'CNY', 0.03199),
('ARS', 'RUP', 0.38057),
/*YEN JAPONES*/
('JPY', 'USD', 0.00756),
('JPY', 'EUR', 0.00683),
('JPY', 'CAD', 0.01007),
('JPY', 'ARS', 1.62244),
('JPY', 'AUD', 0.01113),
('JPY', 'MXN', 0.13628),
('JPY', 'GBP', 0.00603),
('JPY', 'CNY', 0.05181),
('JPY', 'RUP', 0.61747),
/*YUAN CHINO*/
('CNY', 'USD', 0.14586),
('CNY', 'EUR', 0.13196),
('CNY', 'CAD', 0.19427),
('CNY', 'ARS', 31.31247),
('CNY', 'AUD', 0.21520),
('CNY', 'MXN', 2.63019),
('CNY', 'GBP', 0.11648),
('CNY', 'JPY', 19.33510),
('CNY', 'RUP', 11.93345),
/*DOLAR AUSTRALIANO*/
('AUD', 'USD', 0.67873),
('AUD', 'EUR', 0.61320),
('AUD', 'CAD', 0.90417),
('AUD', 'ARS', 145.71164),
('AUD', 'CNY', 4.64679),
('AUD', 'MXN', 12.24201),
('AUD', 'GBP', 0.54126),
('AUD', 'JPY', 89.84613),
('AUD', 'RUP', 55.45223),
/* PESO MEXICANO */
('MXN', 'USD', 0.05551),
('MXN', 'CAD', 0.07397),
('MXN', 'EUR', 0.05018),
('MXN', 'RUP', 4.53413),
('MXN', 'JPY', 7.35488),
('MXN', 'CNY', 0.38120),
('MXN', 'GBP', 0.04428),
('MXN', 'AUD', 0.08175),
('MXN', 'ARS', 11.91242);

select * from tasas_cambio