import sqlite3


class DatabaseHandler:
    def __init__(self, username: str = None, db_mode: str = 'FILE_MODE'):
        self.username = username
        self.mode = db_mode
        self.filename = None
        self.conn = self.create_connection()
        assert self.conn is not None
        self.create_database()

    def create_connection(self):
        conn_input = None
        conn = None
        if self.mode == 'FILE_MODE':
            if not self.username:
                self.filename = 'user_certificates.db'
            elif all([item.isalnum() for item in self.username]):  # only alphanumeric character allowed
                self.filename = f"{self.username}_certificates.db"
            conn_input = self.filename
        elif self.mode == 'MEMORY_MODE':
            conn_input = ':memory:'

        try:
            conn = sqlite3.connect(conn_input, check_same_thread=False)
        except Exception as e:
            print(e)
        return conn

    def create_database(self):
        query = """CREATE TABLE IF NOT EXISTS "Certs" (
                   ID INTEGER PRIMARY KEY, 
                   Certificate TEXT
                   );"""
        self.conn.execute(query)

    def insert_certificate(self, cert_title: str):
        result = self.conn.execute("INSERT INTO Certs (Certificate) VALUES (?)", (cert_title,))
        self.conn.commit()
        return f'New certificate inserted in database --> ID: {result.lastrowid}'

    def remove_certificate(self, cert_title: str):
        self.conn.execute("DELETE FROM Certs WHERE Certificate=(?)", (cert_title,))
        self.conn.commit()
        return f'A certificate removed from the database'

    def get_certificate_with_name(self, cert_title: str):
        query = "SELECT * FROM Certs WHERE Certificate=(?)"
        result = self.conn.execute(query, (cert_title,)).fetchall()
        return result

    def get_all_certificates(self):
        query = "SELECT * FROM Certs"
        result = self.conn.execute(query).fetchall()
        return result

    def __del__(self):
        self.conn.close()
