-- Функция поиска студентов
CREATE OR REPLACE FUNCTION search_students(pattern TEXT)
RETURNS TABLE(
    id INT,
    studentId TEXT,
    studentName TEXT,
    phone TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT s.id, s.studentid, s.studentname, s.phone
    FROM students s
    WHERE s.studentname ILIKE '%' || pattern || '%'
       OR s.phone ILIKE '%' || pattern || '%';
END;
$$;

-- Функция пагинации
CREATE OR REPLACE FUNCTION get_students_page(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, studentId TEXT, studentName TEXT, phone TEXT)
AS $$
BEGIN
    RETURN QUERY
    SELECT s.id, s.studentid, s.studentname, s.phone
    FROM students s
    ORDER BY s.id
    LIMIT p_limit
    OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;