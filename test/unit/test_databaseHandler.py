import os
import pytest
from models import DatabaseHandler


@pytest.fixture()
def clean():
    try:
        os.remove('godel_certificates.db')
    except FileNotFoundError:
        pass


@pytest.fixture
def setup_database(clean, request):
    db = DatabaseHandler(username='godel', db_mode=request.param)
    db.insert_certificate("Godel certificate")
    yield db


@pytest.mark.parametrize('setup_database', ['FILE_MODE', 'MEMORY_MODE'],
                         indirect=True)
class TestDatabaseHandler:
    def test_create_database(self, setup_database):
        db = setup_database
        assert db.username == 'godel'
        if db.mode == 'FILE_MODE':
            assert db.filename == 'godel_certificates.db'
            assert os.path.isfile(db.filename)
        else:
            assert db.filename is None

    def test_get_certificate_with_name(self, setup_database):
        db = setup_database
        cert = db.get_certificate_with_name("Godel certificate")
        assert cert[0][0] == 1
        assert cert[0][1] == "Godel certificate"

    def test_get_all_certificates(self, setup_database):
        db = setup_database
        certs = db.get_all_certificates()
        assert len(certs) == 1
        assert certs[0][0] == 1
        assert certs[0][1] == "Godel certificate"

    def test_insert_certificate(self, setup_database):
        db = setup_database
        db.insert_certificate("Test Certificate")
        certs = db.get_all_certificates()
        assert len(certs) == 2
        assert db.get_certificate_with_name("Test Certificate")[0][0] == 2
        st = "Test Certificate"
        assert db.get_certificate_with_name("Test Certificate")[0][1] == st

    def test_remove_certificate(self, setup_database):
        db = setup_database
        db.remove_certificate("Godel certificate")
        certs = db.get_all_certificates()
        assert len(certs) == 0
