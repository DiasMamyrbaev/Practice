CREATE OR REPLACE PROCEDURE upsert_contacts_v2(
    p_id INT, p_name TEXT, p_email VARCHAR, p_phone VARCHAR, p_type VARCHAR
)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE id = p_id) THEN
        UPDATE contacts SET names = p_name, email = p_email WHERE id = p_id;

        DELETE FROM phones WHERE contact_id = p_id; 

        INSERT INTO phones(contact_id, phone, type) VALUES(p_id, p_phone, p_type);
    ELSE
        INSERT INTO contacts(id, names, email) VALUES(p_id, p_name, p_email);
        INSERT INTO phones(contact_id, phone, type) VALUES(p_id, p_phone, p_type);
    END IF;
END;
$$;


CREATE OR REPLACE PROCEDURE delete_contacts_v2(p_value TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts WHERE names = p_value OR id::TEXT = p_value;
END;
$$;


CREATE OR REPLACE PROCEDURE insert_many_contacts_v2(
    p_ids INT[], p_names TEXT[], p_phones TEXT[]
)
LANGUAGE plpgsql AS $$
DECLARE i INT;
BEGIN
    FOR i IN 1..array_length(p_ids, 1) LOOP
        IF p_phones[i] !~ '^[0-9]{11}$' THEN
            RAISE NOTICE 'Invalid phone format for ID %: %', p_ids[i], p_phones[i];
        ELSE
            INSERT INTO contacts(id, names) VALUES(p_ids[i], p_names[i]) ON CONFLICT (id) DO NOTHING;
            INSERT INTO phones(contact_id, phone, type) VALUES(p_ids[i], p_phones[i], 'mobile');
        END IF;
    END LOOP;
END;
$$;

CREATE OR REPLACE FUNCTION search_contacts(pattern TEXT)
RETURNS TABLE(id INT, names TEXT, email VARCHAR, phone VARCHAR, type VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN 
    RETURN QUERY
    SELECT c.id, c.names, c.email, p.phone, p.type
    FROM contacts c
    LEFT JOIN phones p ON c.id = p.contact_id
    WHERE c.names ILIKE '%' || pattern || '%' 
       OR c.email ILIKE '%' || pattern || '%'
       OR p.phone ILIKE '%' || pattern || '%';
END;
$$;


CREATE OR REPLACE PROCEDURE add_phone(
    p_contact_name VARCHAR, 
    p_phone VARCHAR, 
    p_type VARCHAR
)
LANGUAGE plpgsql AS $$
DECLARE
    v_contact_id INT;
BEGIN
    SELECT id INTO v_contact_id FROM contacts WHERE names = p_contact_name LIMIT 1;
    IF FOUND THEN
        INSERT INTO phones(contact_id, phone, type) VALUES (v_contact_id, p_phone, p_type);
    ELSE
        RAISE NOTICE 'Contact % not found', p_contact_name;
    END IF;
END;
$$;


CREATE OR REPLACE PROCEDURE move_to_group(
    p_contact_name VARCHAR, 
    p_group_name VARCHAR
)
LANGUAGE plpgsql AS $$
DECLARE
    v_group_id INT;
BEGIN
    SELECT id INTO v_group_id FROM groups WHERE name = p_group_name;
    IF NOT FOUND THEN
        INSERT INTO groups(name) VALUES(p_group_name) RETURNING id INTO v_group_id;
    END IF;
    UPDATE contacts SET group_id = v_group_id WHERE names = p_contact_name;
END;
$$;
