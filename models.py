#!/bin/python3


'''
    Module Docstring here
'''


import sqlite3


class DatabaseHandler:
    '''
    Class Docstring here
    '''
    def __init__(self, username: str = None,   # type: ignore
                 db_mode: str = 'FILE_MODE'):
        self.username = username
        self.mode = db_mode
        self.filename = None
        self.conn = self.create_connection()
        assert self.conn is not None
        self.create_database()

    def create_connection(self):
        '''
            Docstring here
        '''
        conn_input = None
        _conn = None
        if self.mode == 'FILE_MODE':
            if not self.username:
                self.filename = 'user_certificates.db'
                # only alphanumeric character allowed
            elif all([item.isalnum() for item in self.username]):
                self.filename = f"{self.username}_certificates.db"
            conn_input = self.filename
        elif self.mode == 'MEMORY_MODE':
            conn_input = ':memory:'

        try:
            _conn = sqlite3.connect(
                conn_input,  # type: ignore
                check_same_thread=False
            )
        except Exception as exc:
            print(exc)
        return _conn

    def create_database(self):
        '''
            Docstring here
        '''
        query = '''CREATE TABLE IF NOT EXISTS "Certs" (
                   ID INTEGER PRIMARY KEY,
                   Certificate TEXT
                   );'''
        if self.conn is not None:
            self.conn.execute(query)

    def insert_certificate(self, cert_title: str):
        '''
            Docstring here
        '''
        sql_cmd = 'INSERT INTO Certs (Certificate) VALUES (?)'
        if self.conn is not None:
            result = self.conn.execute(sql_cmd, (cert_title,))
            self.conn.commit()
            ret = f'New certificate inserted in db --> ID: {result.lastrowid}'
        else:
            ret = 'Insertion of the new certificate failed'
        return ret

    def remove_certificate(self, cert_title: str):
        '''
            Docstring here
        '''
        sql_cmd = 'DELETE FROM Certs WHERE Certificate=(?)'
        if self.conn is not None:
            self.conn.execute(sql_cmd, (cert_title,))
            self.conn.commit()
        return 'A certificate removed from the database'

    def get_certificate_with_name(self, cert_title: str):
        '''
        _summary_

        Args:
            cert_title (str): _description_

        Returns:
            _type_: _description_
        '''

        if self.conn is None:
            raise ValueError('Database connection is None: self.conn is None')

        query = 'SELECT * FROM Certs WHERE Certificate=(?)'
        result = self.conn.execute(query, (cert_title,)).fetchall()
        return result

    def get_all_certificates(self):
        '''
        _summary_

        Returns:
            _type_: _description_
        '''
        if self.conn is None:
            raise ValueError('Database connection is None: self.conn is None')

        query = "SELECT * FROM Certs"
        result = self.conn.execute(query).fetchall()
        return result

    def __del__(self):
        if self.conn is not None:
            self.conn.close()
