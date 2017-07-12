import pymysql.cursors


def connect():
    connection = pymysql.connect(
                            host='127.0.0.1',
                            user='root',
                            password='root',
                            db='dhlpost',
                            cursorclass=pymysql.cursors.DictCursor
                            )
    return connection
