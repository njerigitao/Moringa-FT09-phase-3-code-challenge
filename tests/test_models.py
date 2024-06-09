import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine
from database.setup import create_tables

class TestModels(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        create_tables()

    def test_author_creation(self):
        author = Author("John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        author = Author("John Doe")
        magazine = Magazine("Tech Weekly", "Technology")
        article = Article("Test Title", "Test Content", author, magazine)
        self.assertEqual(article.title, "Test Title")
        self.assertEqual(article.content, "Test Content")
        self.assertEqual(article.author.name, "John Doe")
        self.assertEqual(article.magazine.name, "Tech Weekly")

    def test_magazine_creation(self):
        magazine = Magazine("Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")

if __name__ == "__main__":
    unittest.main()
