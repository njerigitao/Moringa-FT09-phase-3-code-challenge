from database.connection import get_db_connection

class Author:
    def __init__(self, name):
        self._id = None
        self._name = name
        self.save()
    
    def save (self):
        conn = get_db_connection
        cursor = conn.cursor()
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (self._name,))
        self._id = cursor.lastrowid
        conn.commit()
        conn.close()
        
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM articles WHERE author_id = ?', (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return articles
    
    def magazines(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT DISTINCT m.id, m.name, m.category
            FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?           
        ''', (self.id,))
        magazines = cursor.fetchall()
        conn.close()
        return magazines

    def __repr__(self):
        return f'<Author {self.name}>'
