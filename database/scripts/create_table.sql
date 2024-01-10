-- Creating the genre_list table
CREATE TABLE genre_list (
    genre_id SERIAL PRIMARY KEY,
    genre_name VARCHAR(255) NOT NULL
);

-- Creating the movie_list table with a foreign key reference to genre_list
CREATE TABLE movie_list (
    movie_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    genre_id INT REFERENCES genre_list(genre_id)
);
