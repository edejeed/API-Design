-- Create a function to get data from the "colleges" table
CREATE OR REPLACE FUNCTION get_colleges()
RETURNS JSONB AS $$
BEGIN
    RETURN (
        SELECT jsonb_agg(jsonb_build_object(
            'college_id', college_id,
            'college_name', college_name
        ))
        FROM colleges
    );
END;
$$ LANGUAGE plpgsql;


