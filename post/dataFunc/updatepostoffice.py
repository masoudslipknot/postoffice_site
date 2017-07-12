import pymysql.cursors
import connectdb
my_connection =  connectdb.connect()


def updatepostoffice(username , postofficename):
    query  = "UPDATE employee SET employee.postofficename='postofficename' WHERE employee.username='username' and employee.ssn not in (SELECT ssn  FROM   fired  WHERE  fired.FLAG='FALSE') ='{}';".format(username,postofficename)

    cursor = my_connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    result = cursor.fetchall()
    res = ("affected rows = {}".format(cursor.rowcount))
    if len(res)!= 0:
        return True
    elif len(res)==0:
        return False
    return False


