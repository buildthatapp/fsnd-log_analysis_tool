"""Log Analysis Project for Full Stack Nanodegree by Udacity"""
#!/usr/bin/python
import psycopg2
import sys


def three_most_popular_articles():
    """Queries and displays the top three most viewed articles."""
    DBNAME = "news"
    
    connection = psycopg2.connect(database=DBNAME)

    cursor = connection.cursor()

    query = """
            SELECT articles.title,
                   count(*) as article_views
            FROM   log join
                   articles on log.path = '/article/' || articles.slug
            GROUP BY articles.title
            ORDER BY article_views DESC
            LIMIT 3;
            """

    cursor.execute(query)

    results = cursor.fetchall()

    print()
    print('Three most popular articles of all time')
    print('=======================================')

    for result in results:
        print('"{title}" - {count} views'
              .format(title=result[0], count=result[1]))
    print()

    return


def most_popular_authors():
    """Queries and displays the Authors with the most views."""
    DBNAME = "news"
    
    connection = psycopg2.connect(database=DBNAME)

    cursor = connection.cursor()

    query = """
            SELECT authors.name,
                   count(*) as author_views
            FROM   log
                   JOIN articles ON (log.path = '/article/' || articles.slug)
                   JOIN authors ON articles.author = authors.id 
            GROUP BY authors.name
            ORDER BY author_views DESC;
            """

    cursor.execute(query)

    results = cursor.fetchall()


    print()
    print('Three most popular authors')
    print('=======================================')

    for result in results:
        print('"{author}" - {count} views'
              .format(author=result[0], count=result[1]))
    print()

    return

def days_with_high_errors():
    """Queries and displays the days when errors were above 1%."""
    DBNAME = "news"
    
    connection = psycopg2.connect(database=DBNAME)

    cursor = connection.cursor()

    query = """
              WITH total_requests AS (                                                              
                SELECT time::date AS day, count(*)
                FROM log
                GROUP BY time::date
                ORDER BY time::date
              ), number_of_errors AS (
                SELECT time::date AS day, count(*)
                FROM log
                WHERE status <> '200 OK'
                GROUP BY time::date
                ORDER BY time::date
              ), error_rate AS (
                SELECT total_requests.day,
                  number_of_errors.count::float / total_requests.count::float * 100
                  AS error_percent
                FROM total_requests, number_of_errors
                WHERE total_requests.day = number_of_errors.day
              )
            SELECT * FROM error_rate WHERE error_percent > 1;
            """

    cursor.execute(query)

    results = cursor.fetchall()

    print()
    print('Days with over 1% errors')
    print('=======================================')

    for result in results:
        print('"{day}" - {error_rate} errors'
              .format(day=result[0], error_rate=result[1]))
    print()

    return


def go():
    three_most_popular_articles()
    most_popular_authors()
    days_with_high_errors()


if __name__ == '__main__':
    go()
