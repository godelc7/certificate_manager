from main import APP


def test_home():
    """
    GIVEN a Flask app
    WHEN the root page '/' is requested (GET),
    THEN check for a valid response
    """
    with APP.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"Hello Pexonian, trage hier deine Zertifizierungen ein!" in response.data
        assert b"Liste deiner bisherigen Zertifikate:" in response.data
        assert b"Fehler: Deine Zertifikatsbezeichnung is leer" not in response.data
        assert b"Fehler: Nur alpha numerische Zertifikatsbezeichnungen zugelassen" not in response.data
        assert b"Erfolg: Dein neues Zertikat wurde in der Datenbank eingetragen" not in response.data


def test_home_post():
    """
    GIVEN a Flask app
    WHEN the root page '/' is posted (POST),
    THEN check that status code 500 is returned
    """
    with APP.test_client() as test_client:
        response = test_client.post('/')
        assert response.status_code == 500
