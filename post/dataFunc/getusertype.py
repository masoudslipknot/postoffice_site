import pymysql.cursors
import connectdb
my_connection =  connectdb.connect()


def getusertype(username):
    query  = "SELECT user.`type`  FROM user  WHERE user.username ='{}';".format(username)


    cursor = my_connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    result = cursor.fetchall()
    res=result[0]
    if len(res)!= 0:
        return res["type"]
    elif len(res)!=0:
        return  None
    return None