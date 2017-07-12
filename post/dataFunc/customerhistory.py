import pymysql.cursors
import connectdb
my_connection =  connectdb.connect()
def customerhistory(username ) :
    query = "SELECT DISTINCT recid.*  FROM recid,dispatch,user WHERE  recid.tracking_number=dispatch.tracknumber and (user.username=dispatch.user_sender or user.username=dispatch.user_reciver) and user.username ='{}';".format(username)

    cursor = my_connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    result = cursor.fetchall()

    if len(result) != 0:
        return result

    return None