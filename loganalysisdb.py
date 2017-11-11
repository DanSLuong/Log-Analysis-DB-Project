# !/usr/bin/env python

import psycopg2


def connect(query):
    # Attempt to connect to database
    try:
        db = psycopg2.connect(database="news")
        c = db.cursor()
        c.execute(query)
        results = c.fetchall()
        db.close()
        return results
    except BaseException as e:
        # If there is an prints error string from psycopg2 library if
        # there is an exception
        print(e)
        exit(1)


def popular_articles():

    # What are the most popular three articles of all time?
    print("The 3 most popular articles are: ")
    print("{:^35s}".format("Title") + "|" + "{:^10s}".format("Views"))
    results = (connect("""SELECT a.title,
                                COUNT(b.time) AS views
                                FROM articles a, log b
                                WHERE path!='/'
                                AND b.path = concat('/article/', a.slug)
                                GROUP BY title
                                ORDER BY VIEWS DESC
                                LIMIT 3"""))
    for i in results:
        print("{:^35s}".format(str(i[0])) + '|' + "{:^10s}".format(str(i[1])))
    print("")


def popular_authors():
    # Who are the most popular article authors of all time?
    print("The most popular authors are: ")
    print("{:^25s}".format("Author Name") +
          "|" + "{:^10s}".format("Total Views"))
    # Query that joins the
    results = (connect("""SELECT c.name,
                            COUNT(b.time) AS views
                            FROM articles a, log b, authors c
                            WHERE path!='/'
                            AND b.path = concat('/article/', a.slug)
                            AND a.author = c.id
                            GROUP BY c.name
                            ORDER BY views DESC"""))
    for i in results:
        print("{:^25s}".format(str(i[0])) + '|' + "{:^10s}".format(str(i[1])))
    print("")


def error_day():
    # On which days did more than 1% of requests lead to errors?
    print("The days that had more than 1'%' of request be errors were: ")
    print("{:^12s}".format("Date") + "|" + "{:^15s}".format("% Error"))
    # Query that takes the total number of attempted views and number of errors
    # per day and caculuates the percentage of errors for that day
    results = (connect("""SELECT a.date,
                                (CAST(b.COUNT AS FLOAT)/CAST(a.COUNT
                                AS FLOAT))*100 AS percent
                                FROM (SELECT time::timestamp::date AS date,
                                COUNT(*) FROM log GROUP BY date) a,
                                (SELECT time::timestamp::date AS date, COUNT(*)
                                FROM log
                                WHERE status = '404 NOT FOUND' GROUP BY date) b
                                WHERE a.date = b.date
                                AND ((CAST(b.COUNT AS FLOAT)/CAST(a.COUNT
                                AS FLOAT))*100) > 1.0"""))
    for i in results:
        print("{:^12s}".format(str(i[0])) + '|' + "{:^15s}".format(str(i[1])))
    print("")


if __name__ == "__main__":
    popular_articles()
    popular_authors()
    error_day()
