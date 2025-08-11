from flask import Flask, render_template, request, redirect, url_for
from models import db, Contact

app = Flask(__name__)

# Connexion à MySQL via WAMP
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flask_form_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Création des tables
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        new_contact = Contact(name=name, email=email, message=message)
        db.session.add(new_contact)
        db.session.commit()

        return redirect(url_for('success'))

    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/submissions')
def submissions():
    all_contacts = Contact.query.order_by(Contact.created_at.desc()).all()
    return render_template('submissions.html', contacts=all_contacts)

if __name__ == '__main__':
    app.run(debug=True)
