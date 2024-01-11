-- Create a function to get a specific college by ID
CREATE OR REPLACE FUNCTION get_college_by_id(p_college_id INT)
RETURNS JSONB AS $$
BEGIN
    RETURN (
        SELECT jsonb_build_object(
            'college_id', college_id,
            'college_name', college_name
        )
        FROM colleges
        WHERE college_id = p_college_id
    );
END;
$$ LANGUAGE plpgsql;
