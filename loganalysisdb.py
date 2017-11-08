import psycopg2, bleach

DBNAME = "newsdata"

def get_post():
    db = psycopg2.connect(db=DBNAME)
    c = db.cursor()
    c.execute("select * from authors")
    posts = c.fetchall()
    db.close()
    return posts
