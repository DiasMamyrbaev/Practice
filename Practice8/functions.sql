-- Функция для поиска контактов
CREATE OR REPLACE FUNCTION Search_contacts(pattern TEXT)
RETURNS TABLE(
    id TEXT,
    names TEXT,
    phone TEXT
)
LANGUAGE plpgsql 
AS $$
BEGIN 
    RETURN QUERY
    SELECT c.id, c.names, c.phone
    FROM Contacts c
    WHERE c.names ILIKE '%' || pattern || '%' OR c.phone ILIKE '%' || pattern || '%';
END;
$$;

-- Функция для пагинации
CREATE OR REPLACE FUNCTION get_contacts(p_limit INT, p_offset INT)
RETURNS TABLE(id TEXT, names TEXT, phone TEXT)
AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.names, c.phone
    FROM Contacts c
    ORDER BY c.id
    LIMIT p_limit
    OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;
