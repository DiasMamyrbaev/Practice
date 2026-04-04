-- Процедура вставки или обновления
CREATE OR REPLACE PROCEDURE upsert_student(
    p_id TEXT,
    p_name TEXT,
    p_phone TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM students WHERE studentid = p_id) THEN
        UPDATE students
        SET phone = p_phone, studentname = p_name
        WHERE studentid = p_id;
    ELSE
        INSERT INTO students(studentid, studentname, phone)
        VALUES(p_id, p_name, p_phone);
    END IF;
END;
$$;

-- Процедура массовой вставки с проверкой телефона (11 цифр)
CREATE OR REPLACE PROCEDURE insert_many_students(
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
        -- Проверка: только цифры, ровно 11 штук
        IF p_phones[i] !~ '^[0-9]{11}$' THEN
            RAISE NOTICE 'Invalid phone format for ID %: %. Expected 11 digits.', p_ids[i], p_phones[i];
        ELSE
            INSERT INTO students(studentid, studentname, phone)
            VALUES(p_ids[i], p_names[i], p_phones[i])
            ON CONFLICT (studentid) DO NOTHING;
        END IF;
    END LOOP;
END;
$$;

-- Процедура удаления
CREATE OR REPLACE PROCEDURE delete_student(
    p_value TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM students
    WHERE studentname = p_value
       OR phone = p_value;
END;
$$;
