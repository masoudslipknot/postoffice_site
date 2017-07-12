import pymysql.cursors
import connectdb
my_connection = connectdb.connect()
def statebytype(type ) :
    query = "SELECT state   FROM dispatch WHERE dispatch.`type`='{}';".format(type)
    cursor = my_connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    result = cursor.fetchall()
    res = result[0]
    if len(res) != 0:
      return res["state"]

    return None

