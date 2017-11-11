import psycopg2
from datetime import datetime


def connect(query):
    ## Attempt to connect to database
    try:
        db = psycopg2.connect(database="news")
        c = db.cursor()
        c.execute(query)
        results = c.fetchall()
        db.close()
        return results
    except BaseException:
        ## If there is an exception
        print "Error!!!"


def display_results(results):
    


def popular_articles():

    # What are the most popular three articles of all time?
    print "The 3 most popular articles are: "
    display_results(connect(
        "SELECT a.title, COUNT(b.time) AS views FROM articles a, log b WHERE path!='/' AND b.path LIKE '/article/'||a.slug||'%%' GROUP BY title ORDER BY VIEWS DESC LIMIT 3"))


def popular_authors():
    # Who are the most popular article authors of all time?
    print "The most popular authors are: "
    display_results(connect("SELECT c.name, COUNT(b.time) AS views FROM articles a, log b, authors c WHERE path!='/' AND b.path LIKE '/article/'||a.slug||'%%' AND a.author = c.id GROUP BY c.name ORDER BY views DESC"))


def error_day():
    # On which days did more than 1% of requests lead to errors?
    print "The days that had more than 1'%' of request be errors were: "
    display_results(connect("SELECT a.day, a.COUNT AS total, b.COUNT AS errors, (CAST(b.COUNT AS FLOAT)/CAST(a.COUNT AS FLOAT))*100 AS percent FROM (SELECT date_trunc('day', time) AS day, COUNT(*) FROM log GROUP BY day) a, (SELECT date_trunc('day', time) AS day, COUNT(*) FROM log WHERE status = '404 NOT FOUND' GROUP BY day) b WHERE a.day = b.day AND ((CAST(b.COUNT as FLOAT)/CAST(a.COUNT as FLOAT))*100) > 1.0"))


if __name__ == "__main__":
    popular_articles()
    popular_authors()
    error_day()
