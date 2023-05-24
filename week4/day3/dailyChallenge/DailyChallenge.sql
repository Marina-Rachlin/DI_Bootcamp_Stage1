-- Create 2 tables : Customer and Customer profile. They have a One to One relationship.
-- A customer can have only one profile, and a profile belongs to only one customer
-- The Customer table should have the columns : id, first_name, last_name NOT NULL
-- The Customer profile table should have the columns : id, isLoggedIn DEFAULT false (a Boolean), customer_id (a reference to the Customer table)


-- CREATE TABLE Customer (
--   id SERIAL PRIMARY KEY,
--   first_name VARCHAR(50) NOT NULL,
--   last_name VARCHAR(50) NOT NULL
-- );

-- CREATE TABLE Customer_Profile (
--   id SERIAL PRIMARY KEY,
--   isLoggedIn BOOLEAN DEFAULT false,
--   customer_id INTEGER REFERENCES Customer(id)
-- );




-- Insert those customers
-- John, Doe
-- Jerome, Lalu
-- Lea, Rive

-- INSERT INTO Customer (first_name, last_name)
-- VALUES
--   ('John', 'Doe'),
--   ('Jerome', 'Lalu'),
--   ('Lea', 'Rive');



-- Insert those customer profiles, use subqueries
-- John is loggedIn
-- Jerome is not logged in

-- INSERT INTO Customer_Profile (isLoggedIn, customer_id)
-- VALUES
--   (true, (SELECT id FROM Customer WHERE first_name = 'John')),
--   (false, (SELECT id FROM Customer WHERE first_name = 'Jerome'));



-- Use the relevant types of Joins to display:
-- The first_name of the LoggedIn customers

-- SELECT c.first_name FROM customer AS c
-- JOIN customer_profile AS cp ON c.id = cp.customer_id
-- WHERE cp.isLoggedIn = true


-- All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.

-- SELECT c.first_name FROM customer AS c
-- LEFT JOIN customer_profile AS cp ON c.id = cp.customer_id
-- WHERE cp.isLoggedIn = true


-- The number of customers that are not LoggedIn

-- SELECT COUNT(*) FROM customer AS c
-- LEFT JOIN customer_profile AS cp ON c.id = cp.customer_id 
-- WHERE cp.isLoggedIn = false OR cp.isLoggedIn IS NULL





