import pymysql.cursors
import connectdb
my_connection = connectdb.connect()


def avgtime(senderstate,dispachtype):
    query  = "SELECT AVG(recid.time)  FROM recid, dispatch,user,customer_sender,indivisoial_customer,adress WHERE  recid.tracking_number=dispatch.tracknumber  and user.username=customer_sender.username and(dispatch.user_sender=customer_sender.username or dispatch.user_reciver=customer_sender.username or dispatch.user_reciver=indivisoial_customer.username)and adress.post_code=user.address and adress.center_state='{}' and  dispatch.`type` ='{}';".format(senderstate,dispachtype)
    cursor = my_connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    result = cursor.fetchall()
    res=result[0]

    if len(res)!= 0:
        return res["AVG(recid.time)"]

    return 0