from dataclasses import dataclass
import sqlite3

@dataclass
class Category:
    id: int = 0
    name: str =""

@dataclass
class Movie:
    id:int=0
    name: str = ""
    year: int = 0
    minutes: int = 0
    category: Category = None

DB_FILE = "movies.sqlite"

def connect():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def close(conn):
    conn.close()
    print("Database closed")

def create_table(conn):
    cur = conn.cursor()
    query = "CREATE TABLE IF NOT EXISTS categories (id INT PRIMARY KEY, name TEXT)"
    cur.execute(query)
    conn.commit()
    query = "CREATE TABLE IF NOT EXISTS movies (name TEXT PRIMARY KEY, year INT, minutes INT, category INT)"
    cur.execute(query)
    conn.commit()
    print("Table created successfully")

def create_category_entries(conn):
    cur = conn.cursor()
    query = "INSERT INTO categories VALUES (?,?)"
    category_collection = ((1, 'Animation'), (2,'Comedy'), (3, 'History'))
    for i in range(len(category_collection)):
        cur.execute(query, category_collection[i])
    conn.commit()
    print("Category entries inserted.")

def create_movie_entries(conn):
    cur = conn.cursor()
    query = "INSERT INTO movies VALUES (?,?,?,?)"
    movie_collection = (('Spirited Away', 2005, 125,get_category_id('Animation'),
                         ("Aladdin",1992,90,get_category_id('Animation'))))
    for i in range(len(movie_collection)):
        cur.execute(query, movie_collection[i])
    conn.commit()
    print("Movie entries inserted.")

def get_categories(conn):
    cur = conn.cursor()
    query = ("SELECT * FROM categories")
    cur.execute(query)
    result = cur.fetchall()
    return result

def get_category_id(conn, category_name):
    cur = conn.cursor()
    query = (f"SELECT id FROM categories WHERE name = '{category_name}'")
    cur .execute(query)
    result = cur.fetchone()
    if result:
        return result[0]
    else:
        return None

def get_category_name(conn, category_id):
    cur = conn.cursor()
    query = (f"SELECT name FROM categories WHERE id = '{category_id}'")
    cur .execute(query)
    result = cur.fetchone()
    if result:
        return result[0]
    else:
        return None

def make_category_object(conn,id):
    category_name = get_category_name(conn,id)
    return Category(id, category_name)


if __name__ == "__main__":
    conn = connect()
    create_table(conn)
    #create_category_entries(conn)
    #for category in get_categories(conn):
        #print(category['id'], category['name'])
    #print(get_category_name(conn, 2))
    #print(get_category_id(conn, 'Comedy'))
    #print(make_category_object(conn, 1))
    create_movie_entries(conn)
    close(conn)

