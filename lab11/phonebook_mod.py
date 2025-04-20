import psycopg2
import csv

def connect():
    return psycopg2.connect(
        dbname="lab10",
        user="postgres",
        password="youdontknow",
        host="localhost",
        port="5432"
    )

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(20)
        )
    """)
    conn.commit()
    conn.close()

def create_functions_and_procedures():
    conn = connect()
    cur = conn.cursor()


    cur.execute("""
        CREATE OR REPLACE FUNCTION search_pattern(p_pattern TEXT)
        RETURNS TABLE(id INT, name TEXT, phone TEXT)
        AS $$
        BEGIN
            RETURN QUERY
            SELECT * FROM phonebook
            WHERE name ILIKE '%' || p_pattern || '%'
               OR phone ILIKE '%' || p_pattern || '%';
        END;
        $$ LANGUAGE plpgsql;
    """)


    cur.execute("""
        CREATE OR REPLACE PROCEDURE insert_or_update_user(p_name TEXT, p_phone TEXT)
        AS $$
        BEGIN
            IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
                UPDATE phonebook SET phone = p_phone WHERE name = p_name;
            ELSE
                INSERT INTO phonebook(name, phone) VALUES (p_name, p_phone);
            END IF;
        END;
        $$ LANGUAGE plpgsql;
    """)


    cur.execute("""
        CREATE OR REPLACE PROCEDURE bulk_insert_users(p_names TEXT[], p_phones TEXT[], OUT incorrect TEXT[])
        AS $$
        DECLARE
            i INT := 1;
            tmp TEXT[] := ARRAY[]::TEXT[];
        BEGIN
            WHILE i <= array_length(p_names, 1) LOOP
                IF p_phones[i] ~ '^\\d{10,15}$' THEN
                    INSERT INTO phonebook(name, phone) VALUES (p_names[i], p_phones[i]);
                ELSE
                    tmp := array_append(tmp, p_names[i] || ' - ' || p_phones[i]);
                END IF;
                i := i + 1;
            END LOOP;
            incorrect := tmp;
        END;
        $$ LANGUAGE plpgsql;
    """)

    cur.execute("""
        CREATE OR REPLACE FUNCTION get_users_paginated(p_limit INT, p_offset INT)
        RETURNS TABLE(id INT, name TEXT, phone TEXT)
        AS $$
        BEGIN
            RETURN QUERY
            SELECT * FROM phonebook ORDER BY id LIMIT p_limit OFFSET p_offset;
        END;
        $$ LANGUAGE plpgsql;
    """)

    cur.execute("""
        CREATE OR REPLACE PROCEDURE delete_by_name_or_phone(p_value TEXT)
        AS $$
        BEGIN
            DELETE FROM phonebook WHERE name = p_value OR phone = p_value;
        END;
        $$ LANGUAGE plpgsql;
    """)

    conn.commit()
    conn.close()

def insert_from_csv(file_path):
    conn = connect()
    cur = conn.cursor()
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            name, phone = row
            cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    conn.commit()
    conn.close()

def insert_from_input():
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    conn.commit()
    conn.close()

def bulk_insert(names, phones):
    conn = connect()
    cur = conn.cursor()
    cur.callproc("bulk_insert_users", (names, phones))
    incorrect = cur.fetchone()[0]
    if incorrect:
        print("Incorrect entries:")
        for item in incorrect:
            print(item)
    conn.commit()
    conn.close()

def search_by_pattern(pattern):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_pattern(%s)", (pattern,))
    results = cur.fetchall()
    for row in results:
        print(row)
    conn.close()

def get_paginated(limit, offset):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_users_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.close()

def delete_by_name_or_phone(value):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL delete_by_name_or_phone(%s)", (value,))
    conn.commit()
    conn.close()

#убери коментарий для того что бы активировать функцию 
if __name__ == "__main__":
    create_table()
    create_functions_and_procedures()
    # insert_from_input()
    # insert_from_csv("contacts.csv")
    # bulk_insert(["Alice", "Bob"], ["87001111111", "notaphone"])
    # search_by_pattern("Ali")
    # get_paginated(5, 0)
    # delete_by_name_or_phone("Alice")
