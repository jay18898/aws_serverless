# A lambda function to interact with AWS RDS MySQL

import pymysql
import sys


def save_events(event):
    ce = pymysql.connect(host='Enter_RDS_Endpoint', database='Enter_Database_name', user='Enter_username',
                         password='Enter_Password')

    # m,em,pwd,cno)
    query = "INSERT into regtbl(name,contact_no,email_id,password) values('%s','%s','%s','%s')" % (event['name'], event['cno'], event['em'], event['pwd'])
    cr = ce.cursor()
    cr.execute(query)
    ce.commit()

    cr.close()
    ce.close()


def main(event, context):
    save_events(event)

