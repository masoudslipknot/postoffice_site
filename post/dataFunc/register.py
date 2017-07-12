import pymysql.cursors
import connectdb
my_connection =  connectdb.connect()
def rahgiricode(id ) :
    query = "select * from user WHERE id='{}';".format(id)
    cursor = my_connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    result = cursor.fetchall()
    res = None
    if len(result) != 0:
        return result["pass"]

    return False



