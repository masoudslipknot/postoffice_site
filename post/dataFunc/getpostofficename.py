import pymysql.cursors
import connectdb
my_connection = connectdb.connect()


def getpostname():
    query  = "SELECT post_office.name  FROM post_office "
    cursor = my_connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    result = cursor.fetchall()

    if len(result) != 0:
        return result
    elif len(result) == 0:
        return None
    return None

getpostname()