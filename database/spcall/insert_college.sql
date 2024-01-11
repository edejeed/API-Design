-- Create a stored procedure to insert data into the "colleges" table
CREATE OR REPLACE FUNCTION insert_college(
    p_college_name VARCHAR(100)
)
RETURNS VOID AS $$
BEGIN
    INSERT INTO colleges(college_name)
    VALUES (p_college_name);
END;
$$ LANGUAGE plpgsql;

-- Example usage of the stored procedure
SELECT insert_college('CCS');
