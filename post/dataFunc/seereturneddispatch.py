import pymysql.cursors
import connectdb
my_connection =  connectdb.connect()


def seereturneddispatch():
    query  = "SELECT distinct dispatch.* FROM dispatch WHERE dispatch.state='-1' ".format()
    cursor = my_connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    result = cursor.fetchall()
    if len(result)!= 0:
        return result

    return None

seereturneddispatch()

print seereturneddispatch()