-- CREATE TABLE actors (
-- 	actor_id SERIAL PRIMARY KEY,
-- 	first_name VARCHAR(100) NOT NULL,
-- 	last_name VARCHAR(100)NOT NULL,
-- 	date_birth DATE NOT NULL,
-- 	number_oscars SMALLINT NOT NULL DEFAULT 0
-- )

-- INSERT INTO actors (first_name, last_name, date_birth, number_oscars)
-- VALUES 
-- ('Georges', 'Clooney', '1976-03-12', 2),
-- ('Brad', 'Pitt', '1973-05-10', 3),
-- ('Matt', 'Damon', '1970-01-05', 1),
-- ('Angelina', 'Joli', '1980-01-13', 4),
-- ('Selena', 'Gomez', '1985-05-11', 1),
-- ('Margoret', 'Robbie', '1983-06-11', 1),
-- ('Jennifer', 'Aniston', '1990-10-10', 2)

-- 1. Count how many actors are in the table.
-- SELECT COUNT(*) FROM actors;

-- 2. Try to add a new actor with some blank fields. What do you think the outcome will be ?
-- INSERT INTO actors(first_name, last_name, date_birth, number_oscars)
-- VALUES 
-- (NULL, NULL, '1992/01/07', 3)
-- OUTPUT:ERROR:  Failing row contains (9, null, null, 1992-01-07, 3).null value in column "first_name" of relation "actors" violates not-null constraint



