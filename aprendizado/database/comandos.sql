CREATE TABLE flights (
    id SERIAL PRIMARY KEY, /*PRIMARY KEY indica que esta informação será a maneira principal de referencia aquela linha da tabela*/
    origin VARCHAR NOT NULL, /*NOT NULL indica que aquela informação não pode ficar vazia*/
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
);

INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'London', 415);
INSERT INTO flights (origin, destination, duration) VALUES ('Araripina', 'London', 1000);
INSERT INTO flights (origin, destination, duration) VALUES ('New York', 'London', 600);
INSERT INTO flights (origin, destination, duration) VALUES ('London', 'Araripina', 1200);
INSERT INTO flights (origin, destination, duration) VALUES ('Michigan', 'London', 713);

SELECT * FROM flights;
SELECT origin, destination FROM flights;
SELECT * FROM flights WHERE id = 3;
SELECT * FROM flights WHERE origin = 'New York';
SELECT * FROM flights WHERE duration > 500;
SELECT * FROM flights WHERE duration > 500;
SELECT * FROM flights WHERE destination = 'London' AND duration > 500;
SELECT * FROM flights WHERE destination = 'London' OR duration > 500;

SELECT AVG(duration) FROM flights WHERE destination = 'London' OR duration > 500;
SELECT MIN(duration) FROM flights WHERE destination = 'London';
SELECT COUNT(*) FROM flights;

SELECT * FROM flights WHERE origin IN ('New York', 'Lima');

SELECT * FROM flights WHERE origin LIKE '%a%';

SELECT * FROM flights LIMIT;

SELECT * FROM flights ORDER BY duration DESC;
SELECT * FROM flights ORDER BY duration ASC;

SELECT origin, COUNT(*) FROM flights GROUP BY origin;
SELECT origin, COUNT(*) FROM flights GROUP BY origin HAVING COUNT(*) > 1;





UPDATE flights
    SET duration = 430
    WHERE origin = 'New York'
    AND destination = 'London';

DELETE FROM flights WHERE destination = 'Tokyo';



CREATE TABLE passengers (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    flight_id INTEGER REFERENCES flights
);

INSERT INTO passengers (name, flight_id) VALUES ('Alice', 1);
INSERT INTO passengers (name, flight_id) VALUES ('Bob', 1);
INSERT INTO passengers (name, flight_id) VALUES ('Charlie', 2);
INSERT INTO passengers (name, flight_id) VALUES ('Dave', 2);
INSERT INTO passengers (name, flight_id) VALUES ('Daniel', 4);
INSERT INTO passengers (name, flight_id) VALUES ('Frank', 6);
INSERT INTO passengers (name, flight_id) VALUES ('Grace', 6);


SELECT origin, destination, name FROM flights JOIN passengers ON passengers.flight_id = flights.id;
/*
Me dê as colunas (origin, destination e name) da tabela flights e passengers (isso quer dizer que elas tem algum tipo de relação),  sendo que a relação entre elas é que o 

passengers.flight_id é igual flights.id 
*/

SELECT origin, destination, name FROM flights JOIN passengers ON passengers.flight_id = flights.id WHERE name = 'Alice';
/*
Me dê as colunas (origin, destination e name) da tabela flights e passengers (isso quer dizer que elas tem algum tipo de relação),  sendo que a relação entre elas é que o 

passengers.flight_id é igual flights.id 

E o nome tem que ter o valor 'Alice'
*/

SELECT origin, destination, name FROM flights LEFT JOIN passengers ON passengers.flight_id = flights.id;


SELECT flight_id FROM passengers GROUP BY flight_id HAVING COUNT(*) > 1;
/*
Retornará o flight_id (identificação do voo) que tem mais de 1 passageiro
*/

SELECT * FROM flights WHERE id IN (SELECT flight_id FROM passengers GROUP BY flight_id HAVING COUNT(*) > 1);
/*
Retornará todas as colunas da tabela 'flights' no qual o id tenha o mesmo valor dos
flight_id's (identificação do voo) que tem mais de 1 passageiro
*/
