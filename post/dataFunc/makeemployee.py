import pymysql.cursors
import connectdb
my_connection = connectdb.connect()


def makeemployee(centerstate,city,street, postcode, pelate,floor,password,phone,type,name,postofficename,ssn,mobile,email,lastdegree,timestamp,managerusername,officetype,username,sex):
    cursor = my_connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute("INSERT INTO  adress VALUES(%s,%s,%s,%s,%s,%s)",(centerstate,city,street,postcode,pelate,floor))
    result = cursor.fetchall()
    res = ("affected rows = {}".format(cursor.rowcount))
    if len(res)==0:
        print "suck"
        return False
    cursor = my_connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute("INSERT INTO  user VALUES(%s,%s,%s,%s,%s)",(username,postcode,password,phone,type))
    result = cursor.fetchall()
    res = ("affected rows = {}".format(cursor.rowcount))
    if len(res)==0:
        print "fuck"
        return False
    cursor = my_connection.cursor(pymysql.cursors.DictCursor)

    cursor.execute("INSERT INTO  post_office VALUES(%s,%s,%s,%s,%s,%s,%s)",(postofficename,managerusername,officetype,0,0,0,0))
    result = cursor.fetchall()
    cursor = my_connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute("INSERT INTO  employee VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(username,name,postofficename,ssn,mobile,email,lastdegree,timestamp,type,sex))
    result = cursor.fetchall()
    res = ("affected rows = {}".format(cursor.rowcount))
    if len(res) == 0:
        return False

    return True