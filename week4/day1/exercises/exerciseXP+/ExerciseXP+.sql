-- CREATE TABLE students (
-- 	id SERIAL PRIMARY KEY,
-- 	first_name VARCHAR(100) NOT NULL,
-- 	last_name VARCHAR(100) NOT NULL,
-- 	birth_date DATE NOT NULL
-- 	)

-- SET DATESTYLE TO DMY;

-- INSERT INTO students (first_name, last_name, birth_date) VALUES ('Marc',	'Benichou',	'02/11/1998'),
-- ('Yoan',	'Cohen',	'03/12/2010'),
-- ('Lea',	'Benichou',	'27/07/1987'),
-- ('Amelia',	'Dux',	'07/04/1996'),
-- ('David',	'Grez',	'14/06/2003'),
-- ('Omer',	'Simpson',	'03/10/1980')

-- INSERT INTO students (first_name, last_name, birth_date) VALUES ('Marina',	'Rachlin',	'07/01/1992')

-- SELECT * FROM students
	
-- SELECT * FROM students WHERE last_name = 'Benichou' AND first_name = 'Marc'

-- SELECT * FROM students WHERE last_name = 'Benichou' OR first_name = 'Marc'

-- SELECT * FROM students WHERE first_name ILIKE '%a%'

-- SELECT * FROM students WHERE first_name ILIKE 'a%'

-- SELECT * FROM students WHERE first_name LIKE '%a'

-- SELECT * FROM students WHERE first_name LIKE '_%a_'

-- SELECT * FROM students WHERE id IN (1,3)

-- SELECT * FROM students WHERE birth_date >= '2000/01/01'



