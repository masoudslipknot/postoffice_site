import pymysql.cursors
import connectdb
my_connection =  connectdb.connect()
def fire(username ) :
    query = "SELECT employee.ssn, post_office.name FROM employee,user,post_office WHERE  user.username=employee.username and post_office.name=employee.postofficename and employee.username ='{}';".format(username)
    cursor = my_connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    result = cursor.fetchall()
    if len(result) != 0:
     res = result[0]
     postofficename = res["name"]
     employeessn = res["ssn"]
     cursor = my_connection.cursor(pymysql.cursors.DictCursor)
     cursor.execute("INSERT fired VALUES(%s,%s,FALSE)",(str(employeessn),postofficename))
     result = cursor.fetchall()
     my_connection.commit()
     res = ("affected rows = {}".format(cursor.rowcount))
     if len(res) !=0:
        return True
     elif len(res)==0:
        return False

    return False

fire('alireza')
