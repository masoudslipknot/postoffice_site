import pymysql.cursors
import connectdb
import Fireemployee
my_connection =  connectdb.connect()
def makeitworker(username,postofficename ) :
    chkfire = Fireemployee.fire(username)
    if chkfire !=True:
     query = "UPDATE employee  SET employee.employee_type='employee' WHERE employee.username='{}' and employee.postofficename ='{}';".format(username,postofficename)
     cursor = my_connection.cursor(pymysql.cursors.DictCursor)
     cursor.execute(query)
     result = cursor.fetchall()
     res=("affected rows = {}".format(cursor.rowcount))
     if len(res) != 0:
        return True
     query = "UPDATE user  SET user.`type`='employee'  employee.postofficename ='{}';".format(
        username)
     cursor = my_connection.cursor(pymysql.cursors.DictCursor)
     cursor.execute(query)
     if len(res) != 0:
        return True
    elif chkfire==True:
        return False
    return False