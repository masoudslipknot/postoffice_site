import pymysql.cursors

import connectdb

my_connection =  connectdb.connect()
def checkmaneger(username ) :
    query = "SELECT employee.*  FROM user,employee WHERE user.username=employee.username and employee.employee_type=user.`type` and  employee.employee_type='manager' and employee.username ='{}';".format(username)
    cursor = my_connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    result = cursor.fetchall()
    if len(result) != 0:
        return True
    elif len(result)==0 :
        que = "UPDATE employee,user  SET  employee.employee_type='manager' , user.`type`='manager' WHERE user.username=employee.username and employee.username ='{}';".format(
            username)
        cursor = my_connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(que)
        quer = "UPDATE user,employee  SET  employee.employee_type='manager' , user.`type`='manager' WHERE user.username=employee.username and user.username ='{}';".format(
            username)
        cursor = my_connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(quer)
        print "hi"

    return False
