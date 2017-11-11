# Log Analysis Project

### Problem description
>Your task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.
 
### Project Goals
Our aim this project is to answer the following three questions.
1. What are the most popular three articles of all time?
Example:
* "Princess Shellfish Marries Prince Handsome" — 1201 views
* "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
* "Political Scandal Ends In Political Scandal" — 553 views

2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
Example:
* Ursula La Multa — 2304 views
* Rudolf von Treppenwitz — 1985 views
* Markoff Chaney — 1723 views
* Anonymous Contributor — 1023 views
3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)
Example:
* July 29, 2016 — 2.5% errors

### Required Software:

* [Python 3.6](https://www.python.org/downloads/)
* [Virtualbox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
* [Vagrant (Virtual Machine)](https://www.vagrantup.com/downloads.html)
* [PostgreSQL](https://www.postgresql.org/download/)

### Necessary Files:
* FSND-Vitural-Machine Directory from the Udacity Fullstack Nanodegree [link](https://github.com/udacity/fullstack-nanodegree-vm)
* The database file - [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
* A zip with the files contained in this [repository](https://github.com/DanSLuong/Log-Analysis-DB-Project)

### Instructions:
1. Start the Vagrant VM inside of the 
```~/FSND-Virtual-Machine/vagrant/``` 
by entering the following command into the terminal:

  >```$ vagrant up```

This may take a few minutes because your pc will download a whole OS.

2. Login to the virtual machine by inputing into the terminal:

  >```$ vagrant ssh```

3. Extract the zip file content into the same folder that you have your newsdata.sql file.
4. Move into the folder with all of our project files using the command:

  >```$ cd /vagrant/Log-Analysis-DB-Project/```

5. Load the SQL file into a local database using the command:

  >```$ psql -d news -f newsdata.sql```

6. In the terminal, enter the following command:

  >```$ python loganalysisdb.py```

