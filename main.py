import socket
from flask import Flask, request, render_template, flash
from models import DatabaseHandler

DATABASE = None

APP = Flask(__name__)
APP.config['SECRET_KEY'] = 'wertivicwdfkjk_fwr924/§$=)("?§'
HOSTNAME = socket.gethostname()


def handle_cert_title(title):
    if len(title) == 0:
        flash('Fehler: Deine Zertifikatsbezeichnung is leer', category='error')
    elif not all([item.isalnum() or item.isspace() or
                 item in ('(', ')', '-', '_') for item in title]):
        msg = 'Fehler: Nur alphanumerische Zertifikatsbezeichnungen zugelassen'
        flash(msg, category='error')
    elif len(title) < 4:
        msg = 'Fehler: Zertifikatsbezeichnungen müssen mindestens '
        msg += ' 4 Zeichen enthalten'
        flash(msg, category='error')
    else:
        if DATABASE is not None:
            DATABASE.insert_certificate(title)
            msg = 'Erfolg: Dein neues Zertifikat wurde '
            msg += 'in der Datenbank eingetragen'
            flash(msg, category='success')


@APP.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':  # type: ignore
        cert_title = request.form.get('certificate')  # type: ignore
        handle_cert_title(cert_title)

    if DATABASE is None:
        return render_template("home.html")
    return render_template("home.html",
                           certificates=DATABASE.get_all_certificates(),
                           hostname=HOSTNAME)


@APP.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html", hostname=HOSTNAME)


@APP.route("/sign_up", methods=['GET', 'POST'])
def sign_up():
    return render_template("sign_up.html", hostname=HOSTNAME)


if __name__ == '__main__':
    DATABASE = DatabaseHandler()
    APP.run(host='0.0.0.0', debug=True)
