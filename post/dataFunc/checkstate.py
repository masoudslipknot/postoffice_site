import pymysql.cursors
import connectdb
my_connection =  connectdb.connect()
def rahgiricode(trackingnumber ) :
    query = "SELECT dispatch.*  FROM dispatch,recid WHERE recid.tracking_number=dispatch.tracknumber and tracknumber ='{}';".format(trackingnumber)
    cursor = my_connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    result = cursor.fetchall()

    if len(result) != 0:
      return result[0]

    return None

