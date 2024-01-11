-- Create a function to update a specific college by ID
CREATE OR REPLACE FUNCTION update_college_by_id(
    p_college_id INT,
    p_college_name VARCHAR(100)
)
RETURNS VOID AS $$
BEGIN
    UPDATE colleges
    SET
        college_name = p_college_name
    WHERE
        college_id = p_college_id;
END;
$$ LANGUAGE plpgsql;
