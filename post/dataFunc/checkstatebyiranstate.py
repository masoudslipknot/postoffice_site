import pymysql.cursors

import connectdb

my_connection = connectdb.connect()
def statebystate(centerstate ) :
    query = "SELECT state   FROM dispatch,user,adress  WHERE dispatch.user_sender=user.username and user.address=adress.post_code and adress.center_state='{}';".format(centerstate)
    cursor = my_connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    result = cursor.fetchall()

    if len(result) != 0:
      return result

    return None

