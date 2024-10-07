from flask import Flask, render_template, request, redirect, url_for
from models import init_db, add_contact, get_contacts

app = Flask(__name__)

# Инициализация базы данных
init_db()

@app.route('/')
def index():
    contacts = get_contacts()
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('name')
    phone = request.form.get('phone')
    if name and phone:
        add_contact(name, phone)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
