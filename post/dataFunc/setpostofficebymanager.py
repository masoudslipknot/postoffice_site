import pymysql.cursors
import connectdb
import datetime
my_connection =  connectdb.connect()
def setbymanager(postofficename,username ) :
    query = "UPDATE employee,user SET employee.postofficename='{}' WHERE   employee.username=user.username and employee.username='{}';".format(postofficename,username)
    cursor = my_connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    result = cursor.fetchall()
    res = ("affected rows = {}".format(cursor.rowcount))
    query = "SELECT employee.ssn FROM   employee,user  WHERE  user.username=employee.username  and employee.username='{}';".format(username)
    cursor = my_connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    result = cursor.fetchall()
    res = result[0]
    ssn = res['ssn']
    now = datetime.datetime.now();

    cursor = my_connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute("INSERT INTO historyofemployee  VALUES (%s, %s, %s)", (str(ssn), now.isoformat(),postofficename ))
    result = cursor.fetchall()
    res = ("affected rows = {}".format(cursor.rowcount))
    if len(res) != 0:
        return True
    elif len(res) == 0:
        return False
    return False

