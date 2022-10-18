import sys
import os
dir_name = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.split(os.path.split(dir_name)[0])[0])
from main import APP  # noqa: E402


def test_home():
    """
    GIVEN a Flask app
    WHEN the root page '/' is requested (GET),
    THEN check for a valid response
    """
    with APP.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"Hello Nutzer, trage hier deine Zertifizierungen ein!" in \
            response.data
        assert b"Liste deiner bisherigen Zertifikate:" in response.data
        assert b"Fehler: Deine Zertifikatsbezeichnung is leer" not in \
            response.data
        assert b"Fehler: Nur alpha numerische Zertifikatsbezeichnungen \
            zugelassen" not in response.data
        assert b"Erfolg: Dein neues Zertifikat wurde in der Datenbank \
            eingetragen" not in response.data


def test_home_post():
    """
    GIVEN a Flask app
    WHEN the root page '/' is posted (POST),
    THEN check that status code 500 is returned
    """
    with APP.test_client() as test_client:
        response = test_client.post('/')
        assert response.status_code == 500


def test_login():
    """
    GIVEN a flask application
    WHEN the page '/login' is requested (GET)
    THEN check for a valid response
    """
    with APP.test_client() as test_client:
        response = test_client.get('/login')
        assert response.status_code == 200
        res_data = response.data
        assert b"Site under construction, this form is useless!!" in res_data
        assert b"Email Address" in response.data
        assert b"Password" in response.data


def test_login_post():
    """
    GIVEN a Flask app
    WHEN the page '/login' is posted (POST),
    THEN check for a valid response
    """
    with APP.test_client() as test_client:
        response = test_client.post('/login')
        assert response.status_code == 200
        assert b"Email Address" in response.data
        assert b"Password" in response.data


def test_sign_up():
    """
    GIVEN a flask application
    WHEN the page '/sign_up' is requested (GET)
    THEN check for a valid response
    """
    with APP.test_client() as test_client:
        response = test_client.get('/sign_up')
        assert response.status_code == 200
        res_data = response.data
        assert b"Site under construction, this form is useless!!" in res_data
        assert b"First and last Name:" in response.data


def test_sign_up_post():
    """
    GIVEN a Flask app
    WHEN th page '/sign_up' is posted (POST),
    THEN check for a valid response
    """
    with APP.test_client() as test_client:
        response = test_client.post('/sign_up')
        assert response.status_code == 200
        res_data = response.data
        assert b"Site under construction, this form is useless!!" in res_data
        assert b"First and last Name:" in response.data
