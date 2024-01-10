-- Creating the function
CREATE OR REPLACE FUNCTION insert_genre_data(
    p_genre_name VARCHAR(255)
)
RETURNS VOID
AS $$
BEGIN
    -- Inserting data into genre_list table if genre does not exist
    INSERT INTO genre_list (genre_name) 
    VALUES (p_genre_name);
END;
$$
LANGUAGE plpgsql;

-- Example usage
SELECT insert_genre_data('Action');

