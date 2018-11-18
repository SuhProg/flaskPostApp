import sqlite3 as sql
from os import path

# getting the direc name and its path
ROOT = path.dirname(path.relpath(__file__))

def create_post(name, content):
    con = sql.connect(path.join(ROOT, 'network.db'))
    # instead of getting the whole database, grabs just what's needed
    cur = con.cursor()
    # executing raw sql sintax
    cur.execute('INSERT INTO posts (name, content) values(?, ?)', (name, content))
    # commiting changes to the database
    con.commit()
    # closing the connection to the database
    con.close()

# get the posts requested from the data base so they can be displayed at the frontend
def get_posts():
    con = sql.connect(path.join(ROOT, 'network.db'))
    cur = con.cursor()
    cur.execute('SELECT * FROM posts')
    posts = cur.fetchall()
    return posts
