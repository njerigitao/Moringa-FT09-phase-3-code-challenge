from database.connection import get_db_connection

class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category
        self.save()
    
    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (self._name, self._category))
        self._id = cursor.lastrowid
        conn.commit()
        conn.close()
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        self._category = value
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE magazines SET category = ? WHERE id = ?', (value, self.id))
        conn.commit()
        conn.close()
    
    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM articles WHERE magazine_id = ?', (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return articles


    def __repr__(self):
        return f'<Magazine {self.name}>'
