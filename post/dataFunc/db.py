import pymysql.cursors
import connectdb
my_connection =  connectdb.connect()


def fetch_user(username , password):
    query  = "select * from user WHERE username='{}';".format(username)
    cursor = my_connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    result = cursor.fetchall()

    res = None
    if len(result)!= 0 :
        res = result[0]
        if res["pass"] == password :
            return True
        else :
            return False
    return False


