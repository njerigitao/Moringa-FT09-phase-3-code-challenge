from database.connection import get_db_connection
from models.author import Author
from models.magazine import Magazine

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = None
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id
        self.save()
    
    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO articles (title, content, author_id, magazine_id)
            VALUES (?, ?, ?, ?)           
        ''', (self._title, self._content, self._author.id, self._magazine.id))
        self._id = cursor.lastrowid
        conn.commit()
        conn.close()
    


    def __repr__(self):
        return f'<Article {self.title}>'
