from database.connection import get_db_connection

class Magazine:
    def __init__(self, name, category):
        self._id = None
        self._name = name
        self._category = category
        self.save()
    
    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (self._name, self._category))
        self._id = cursor.lastrowid
        conn.commit()
        conn.close()
    
    @property
    def id(self):
        return self._id
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
        conn = get_db_connection
        cursor = conn.cursor()
        cursor.execute()
    
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
    
    def contributors(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT DISTINCT authors.* FROM authors
            JOIN articles ON authors.id = articles.author_id
            WHERE articles.magazine_id = ?
        ''', (self.id,))
        authors = cursor.fetchall()
        conn.close()
        return authors
    
    def article_titles(self):
        conn = get_db_connection
        cursor = conn.cursor()
        cursor.execute('SELECT title FROM articles WHERE magazine_id = ?', (self.id,))
        titles = [row['title'] for row in cursor.fetchall()]
        conn.close()
        return titles
    
    def contributing_authors(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT authors.* FROM authors
            JOIN articles ON authors.id = articles.author_id
            WHERE articles.magazine_id = ?
            GROUP BY authors.id
            HAVING COUNT(articles.id) > 2
       ''', (self.id,))
        authors = cursor.fetchall()
        conn.close()
        return authors

    def __repr__(self):
        return f'<Magazine {self.name}, {self.category}>'
