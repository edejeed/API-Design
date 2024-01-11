-- Delete a specific college by ID
CREATE OR REPLACE FUNCTION delete_college_by_id(p_college_id INT)
RETURNS VOID AS $$
BEGIN
    DELETE FROM colleges WHERE college_id = p_college_id;
END;
$$ LANGUAGE plpgsql;
