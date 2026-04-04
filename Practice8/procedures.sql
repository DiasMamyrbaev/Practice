-- Процедура для добавления или обновления
CREATE OR REPLACE PROCEDURE upsert_contacts(
    p_id TEXT,
    p_name TEXT,
    p_phone TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM Contacts WHERE id = p_id) THEN
        UPDATE Contacts
        SET phone = p_phone, names = p_name
        WHERE id = p_id;
    ELSE
        INSERT INTO Contacts(id, names, phone)
        VALUES(p_id, p_name, p_phone);
    END IF;
END;
$$;

-- Процедура для массовой вставки
CREATE OR REPLACE PROCEDURE insert_many_contacts(
    p_ids TEXT[],
    p_names TEXT[],
    p_phones TEXT[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(p_ids, 1)
    LOOP
        -- Проверка на 11 цифр
        IF p_phones[i] !~ '^[0-9]{11}$' THEN
            RAISE NOTICE 'Invalid phone format for ID %: %', p_ids[i], p_phones[i];
        ELSE
            INSERT INTO Contacts(id, names, phone)
            VALUES(p_ids[i], p_names[i], p_phones[i])
            ON CONFLICT (id) DO NOTHING;
        END IF;
    END LOOP;
END;
$$;

-- Процедура для удаления
CREATE OR REPLACE PROCEDURE delete_contacts(
    p_value TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM Contacts
    WHERE names = p_value
       OR phone = p_value
       OR id = p_value;
END;
$$;
