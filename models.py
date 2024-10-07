import psycopg2

DATABASE_URL = 'your_postgresql_connection_string'  # Строка подключения к базе данных

def init_db():
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(15)
        )
    ''')
    conn.commit()
    conn.close()

def add_contact(name, phone):
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    conn.close()

def get_contacts():
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("SELECT name, phone FROM contacts")
    contacts = cursor.fetchall()
    conn.close()
    return contacts
