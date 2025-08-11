# 📬 Flask MySQL Contact Form (WAMP Ready)

### Description
This is a simple Flask web application that collects contact form data and stores it in a **MySQL database via WAMP**.

### Features
- Contact form with name, email, message
- Stores in MySQL (WAMP)
- View all submissions in a table
- Bootstrap layout

### Requirements
- Python 3.x
- WAMP with MySQL running (http://localhost/phpmyadmin)
- Flask, Flask-SQLAlchemy, PyMySQL

### Installation
```bash
git clone https://github.com/ecomdesignbe/flask-form-wamp.git
cd flask-form-wamp
pip install -r requirements.txt

### MySQL Setup (via phpMyAdmin)
```bash
Open http://localhost/phpmyadmin

Create database: flask_form_db

Use user root (no password by default)

Run the app
bash
Copier
Modifier
python app.py
Go to: http://127.0.0.1:5000