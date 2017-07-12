import pymysql.cursors
import connectdb
my_connection =  connectdb.connect()
def employeesex( ) :
    query = "SELECT  distinct employee.* FROM   employee,user  WHERE  employee.username=user.username ORDER BY employee.sex ;"
    cursor = my_connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    result = cursor.fetchall()

    if len(result) != 0:
      return result

    return None

