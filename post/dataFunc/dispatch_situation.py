import pymysql.cursors
import connectdb
my_connection =  connectdb.connect()
def returnsituation(trackingnumber ) :
    query = "SELECT dispatch.*  FROM dispatch,recid  WHERE dispatch.tracknumber=recid.tracking_number and recid.tracking_number ='{}';".format(trackingnumber)
    cursor = my_connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    result = cursor.fetchall()

    if len(result) != 0:
            return result

    return None