from flask import Flask, request, render_template, flash
from models import DatabaseHandler

DATABASE = None

APP = Flask(__name__)
APP.config['SECRET_KEY'] = 'wertivicwdfkjk_fwr924/§$=)("?§'


def handle_cert_title(title):
    if len(title) == 0:
        flash('Fehler: Deine Zertifikatsbezeichnung is leer', category='error')
    elif not all([item.isalnum() or item.isspace() or item in ('(', ')', '-', '_') for item in title]):
        flash('Fehler: Nur alphanumerische Zertifikatsbezeichnungen zugelassen', category='error')
    elif len(title) < 4:
        flash('Fehler: Zertifikatsbezeichnungen müssen mindestens 4 Zeichen enthalten', category='error')
    else:
        DATABASE.insert_certificate(title)
        flash('Erfolg: Dein neues Zertifikat wurde in der Datenbank eingetragen', category='success')


@APP.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        cert_title = request.form.get('certificate')
        handle_cert_title(cert_title)

    if DATABASE is None:
        return render_template("home.html")
    return render_template("home.html", certificates=DATABASE.get_all_certificates())


@APP.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@APP.route("/sign_up", methods=['GET', 'POST'])
def sign_up():
    return render_template("sign_up.html")


if __name__ == '__main__':
    DATABASE = DatabaseHandler()
    APP.run(host='0.0.0.0', debug=True)
