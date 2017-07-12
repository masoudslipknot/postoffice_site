import pymysql.cursors


def connect():
    connection = pymysql.connect(
                            host='127.0.0.1',
                            user='root',
                            password='12341234',
                            db='dhlpost',
                            port=3355,
                            cursorclass=pymysql.cursors.DictCursor
                            )
    return connection
