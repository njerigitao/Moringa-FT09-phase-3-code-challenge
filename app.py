from database.setup import create_tables
#from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    # Connect to the database
    #conn = get_db_connection()
    #cursor = conn.cursor()


    '''
        The following is just for testing purposes, 
        you can modify it to meet the requirements of your implmentation.
    '''

    # Create an author
    #cursor.execute('INSERT INTO authors (name) VALUES (?)', (author_name,))
    #author_id = cursor.lastrowid # Use this to fetch the id of the newly created author
    author = Author(author_name)

    # Create a magazine
    magazine = Magazine(magazine_name, magazine_category)
    #cursor.execute('INSERT INTO magazines (name, category) VALUES (?,?)', (magazine_name, magazine_category))
    #magazine_id = cursor.lastrowid # Use this to fetch the id of the newly created magazine

    # Create an article
    article = Article(article_title, article_content, author, magazine)
    #cursor.execute('INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)',
                   #(article_title, article_content, author_id, magazine_id))

    #conn.commit()

    # Query the database for inserted records. 
    # The following fetch functionality should probably be in their respective models

    #cursor.execute('SELECT * FROM magazines')
    #magazines = cursor.fetchall()

    #cursor.execute('SELECT * FROM authors')
    #authors = cursor.fetchall()

    #cursor.execute('SELECT * FROM articles')
    #articles = cursor.fetchall()

    #conn.close()

    # Display results
    print("\nMagazines:")
    magazines = author.magazines()
    for mag in magazines:
        print(mag)
    #for magazine in magazines:
        #print(Magazine(magazine["id"], magazine["name"], magazine["category"]))

    print("\nAuthors:")
    authors = author.articles()
    for article in authors:
        print(article)
    #for author in authors:
        #print(Author(author["id"], author["name"]))

    print("\nArticles:")
    articles = magazine.articles()
    for art in articles:
        print(art)
    #for article in articles:
        #print(Article(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]))
    print("\nMagazine Contributors:")
    contributors = magazine.contributors()
    for contributor in contributors:
        print(contributor)

if __name__ == "__main__":
    main()
