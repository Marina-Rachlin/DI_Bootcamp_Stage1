-- 🌟 Exercise 1: DVD Rental
-- Instructions
-- Get a list of all film languages.

-- SELECT name FROM language



-- Get a list of all films joined with their languages – select the following details : film title, description, and language name. Try your query with different joins:
-- Get all films, even if they don’t have languages.

-- SELECT title, description, language.name
-- FROM film
-- LEFT OUTER JOIN language
-- ON film.language_id = language.language_id;



-- Get all languages, even if there are no films in those languages.

-- SELECT l.name, f.title, f.description
-- FROM film as f
-- RIGHT OUTER JOIN language As l
-- ON f.language_id = l.language_id;



-- Create a new table called new_film with the following columns : id, name. Add some new films to the table.

-- CREATE TABLE new_film(
-- id serial PRIMARY KEY,
-- name VARCHAR(255)
-- )
	
-- INSERT INTO new_film (name) VALUES
-- ('Interstellar'),
-- ('Tenet'),
-- ('Dr. House');
	
	
	
-- Create a new table called customer_review, which will contain film reviews that customers will make.
-- Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.
-- It should have the following columns:
-- review_id – a primary key, non null, auto-increment.
-- film_id – references the new_film table. The film that is being reviewed.
-- language_id – references the language table. What language the review is in.
-- title – the title of the review.
-- score – the rating of the review (1-10).
-- review_text – the text of the review. No limit on the length.
-- last_update – when the review was last updated.

-- CREATE TABLE customer_review (
--   review_id serial PRIMARY KEY,
--   film_id integer REFERENCES new_film (id) ON DELETE CASCADE,
--   language_id integer REFERENCES language (language_id),
--   title VARCHAR(255),
--   score integer,
--   review_text TEXT,
--   last_update TIMESTAMP
-- );



-- Add 2 movie reviews. Make sure you link them to valid objects in the other tables.

-- INSERT INTO customer_review (film_id, language_id, title, score, review_text, last_update)
-- VALUES
-- (1, 1, 'Review 1', 10, 'This is the first review',  CURRENT_TIMESTAMP)
 
 
 

-- Delete a film that has a review from the new_film table, what happens to the customer_review table?

-- DELETE FROM new_film WHERE name = 'Interstellar'
-- SELECT * FROM customer_review 

-- After the film was deleted the review was deleted too



-- 🌟 Exercise 2 : DVD Rental
-- Instructions
-- Use UPDATE to change the language of some films. Make sure that you use valid languages.

-- UPDATE film
-- SET language_id = 2
-- WHERE film_id BETWEEN 1 AND 5;



-- Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?
-- The presence of foreign keys in the customer table affects the way in which you INSERT into the table. When inserting data into a table that has foreign key constraints, you need to ensure that the values you provide for the foreign key columns match existing values in the referenced tables. Otherwise, the insert operation will fail due to a foreign key constraint violation.




-- We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
-- DROP TABLE customer_review;

-- Its easy to drop a table. But it's very important to ensure that we no longer need the data in the table because dropping the table will permanently remove all its data.




-- Find out how many rentals are still outstanding (ie. have not been returned to the store yet).

-- SELECT COUNT (*) FROM rental WHERE return_date IS NULL



-- Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)

-- SELECT film.film_id, film.title, film.replacement_cost FROM rental 
-- INNER JOIN inventory ON rental.inventory_id = inventory.inventory_id
-- LEFT JOIN film ON inventory.film_id = film.film_id
-- WHERE rental.return_date IS NULL
-- ORDER BY film.replacement_cost DESC LIMIT 30



-- Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
-- The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.

-- SELECT f.film_id, f.title, f.description, a.first_name, a.last_name FROM film AS f
-- JOIN film_actor AS fa ON f.film_id = fa.film_id
-- JOIN actor AS a ON a.actor_id = fa.actor_id
-- WHERE f.description ILIKE '%sumo wrestler%'  AND a.first_name = 'Penelope' AND a.last_name = 'Monroe'



-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.

-- SELECT f.film_id, f.title, f.length, c.name, f.rating FROM film AS f
-- JOIN film_category AS fc ON f.film_id = fc.film_id
-- JOIN category AS c ON fc.category_id = c.category_id
-- WHERE f.length < 60 AND f.rating = 'R' AND c.name = 'Documentary'




-- The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.

-- SELECT f.title, p.amount, r.return_date,c.first_name, c.last_name FROM film AS f
-- JOIN inventory AS i ON f.film_id = i.film_id
-- JOIN rental AS r ON i.inventory_id = r.inventory_id
-- JOIN customer AS c ON r.customer_id = c.customer_id
-- JOIN payment AS p ON r.rental_id = p.rental_id
-- WHERE c.first_name = 'Matthew' AND c.last_name = 'Mahan' AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01' AND p.amount > 4


--The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.

-- SELECT film.title, film.description, film.replacement_cost, customer.first_name, customer.last_name FROM inventory
-- INNER JOIN film ON film.film_id = inventory.film_id
-- INNER JOIN rental ON rental.inventory_id = inventory.inventory_id
-- INNER JOIN customer ON customer.customer_id = rental.customer_id
-- WHERE customer.first_name = 'Matthew'
-- AND customer.last_name = 'Mahan'
-- AND (film.title ILIKE '%boat%' OR film.description ILIKE '%boat%')
-- ORDER BY film.replacement_cost DESC LIMIT 1



