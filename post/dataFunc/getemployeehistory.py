import pymysql.cursors
import connectdb
my_connection =  connectdb.connect()
def getemployerhistory(username ) :
    query = "SELECT historyofemployee.*  FROM  historyofemployee,employee,user WHERE employee.username=user.username and historyofemployee.employeessn=employee.ssn and employee.username ='{}';".format(username)

    cursor = my_connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    result = cursor.fetchall()

    if len(result) != 0:
      return result

    return None

