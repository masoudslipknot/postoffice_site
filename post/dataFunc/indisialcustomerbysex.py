import pymysql.cursors

import connectdb

my_connection =  connectdb.connect()
def bysex() :
    query = "SELECT indivisoial_customer.* FROM  indivisoial_customer ORDER BY indivisoial_customer.degree  "
    cursor = my_connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    result = cursor.fetchall()

    if len(result) != 0:
        return result

    return None