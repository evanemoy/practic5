from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os 

app = Flask(__name__)

# Создание базы данных
def init_db():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Главная страница с выводом контактов
@app.route('/')
def index():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('SELECT * FROM contacts')
    contacts = c.fetchall()
    conn.close()
    return render_template('index.html', contacts=contacts)

# Добавление нового контакта
@app.route('/add', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        data = request.get_json()  # Получаем данные в формате JSON
        name = data.get('name')
        phone = data.get('phone')
        conn = sqlite3.connect('contacts.db')
        c = conn.cursor()
        c.execute('INSERT INTO contacts (name, phone) VALUES (?, ?)', (name, phone))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

# Удаление контакта
@app.route('/delete/<int:id>')
def delete_contact(id):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('DELETE FROM contacts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 5000))  # Render использует переменную PORT
    app.run(host='0.0.0.0', port=port)
