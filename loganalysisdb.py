import psycopg2, bleach

DBNAME = "news"

def get_data():
    db = psycopg2.connect(db=DBNAME)
    c = db.cursor()
    c.execute("select * from authors")
    ## What are the most popular three articles of all time?
    ## create view numofviews as select path, count(time) as views from log where path!='/' group by path order by views desc;
    ## select articles.title, numofviews.views from articles, numofviews where numofviews.path = ('/article/'||articles.slug) group by articles.title, numofviews.views order by numofviews.views desc limit 3;
    
    ## Who are the most popular article authors of all time? 
    ## create view authorarticleinfo as select authors.name, articles.title, articles.slug from authors, articles where authors.id=articles.author group by articles.title, articles.slug, authors.name order by authors.name;
    ## select a.name, count(a.name) as views from authorarticleinfo a, log b where b.path=('/article/'||a.slug) and b.path!='/' group by a.name order by views desc;

    ## On which days did more than 1% of requests lead to errors?
    
    posts = c.fetchall()
    db.close()
    return posts