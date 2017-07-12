import pymysql.cursors
import connectdb
my_connection =  connectdb.connect()


def seereturneddispatch(state,tracknumber):
    query  = "UPDATE dispatch,recid SET   dispatch.state='{}' WHERE recid.tracking_number=dispatch.tracknumber and recid.tracking_number ='{}';".format(state,tracknumber)

    cursor = my_connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    result = cursor.fetchall()
    my_connection.commit()
    res = ("affected rows = {}".format(cursor.rowcount))
    if len(res) != 0:
        return True
    elif len(res) == 0:
        return False
    return False

#print seereturneddispatch(12 , 5)