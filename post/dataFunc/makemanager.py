import pymysql.cursors
import connectdb
import Fireemployee
my_connection =  connectdb.connect()

def makeitmanager(username,postofficename ) :
    ckfire = Fireemployee.fire(username)
    if ckfire != True :
     query = "UPDATE employee  SET employee.employee_type='manager' WHERE employee.username='{}' and employee.postofficename ='{}';".format(username,postofficename)
     cursor = my_connection.cursor(pymysql.cursors.DictCursor)
     cursor.execute(query)
     result = cursor.fetchall()
     res=("affected rows = {}".format(cursor.rowcount))
     if len(res) != 0:
         return True
     query = "UPDATE user  SET user.`type`='manager'  employee.postofficename ='{}';".format(
        username)
     cursor = my_connection.cursor(pymysql.cursors.DictCursor)
     cursor.execute(query)
     if len(res) != 0:
         return True
     elif ckfire ==True :
         return False
    return False