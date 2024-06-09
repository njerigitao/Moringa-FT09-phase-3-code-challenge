from .connection import get_db_connection

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        conn = get_db_connection
        cursor = conn.cursor()
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (self._name,))
        self._id = cursor.lastrowid
        conn.commit()
        conn.close()

    def __repr__(self):
        return f'<Author {self.name}>'
