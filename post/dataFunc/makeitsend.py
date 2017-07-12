import pymysql.cursors
import connectdb
my_connection =  connectdb.connect()
def makeitsend(trackingnumber ) :
    query = "UPDATE dispatch,recid  SET state=2 WHERE dispatch.tracknumber=recid.tracking_number and dispatch.tracknumber ='{}';".format(trackingnumber)
    cursor = my_connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    result = cursor.fetchall()
    res=("affected rows = {}".format(cursor.rowcount))
    if len(res) != 0:
        return True

    return False