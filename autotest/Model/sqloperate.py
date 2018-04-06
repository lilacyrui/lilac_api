import time

import MySQLdb
import requests
from jbhautotest.autotest.Data.basicdate import datainfo
from jbhautotest.autotest.Model.timeinfo import createdate
import datetime


#测试数据库连接
def connectsql(db_name):
    try:
        if db_name == datainfo.xboss_db_name:
            conn = MySQLdb.connect(host = datainfo.xboss_host, port = datainfo.port, user = datainfo.xboss_username,
                               passwd = datainfo.xboss_password, db = datainfo.xboss_database, charset = datainfo.charset )
        elif db_name == datainfo.loan_db_name:
            conn = MySQLdb.connect(host=datainfo.loanjbh_host, port=datainfo.port, user=datainfo.loanjbh_username,
                               passwd=datainfo.loanjbh_password, db=datainfo.loanjbh_database, charset=datainfo.charset)
        else:
            print("请选择数据库")
    except:
        pass
    return conn

def updatesql(db_name, sql):
    conn = connectsql(db_name)
    cur = conn.cursor()
    try:
        cur.execute(sql)
        cur.close()
        conn.commit()
    except:
        conn.rollback()
    conn.close()

def insertsql(db_name, sql):
    conn = connectsql(db_name)
    cur = conn.cursor()
    try:
        cur.execute(sql)
        cur.close()
        conn.commit()
    except:
        conn.rollback()
    conn.close()

def selectsql(db_name, sql, fetchtype,listindex):
    conn = connectsql(db_name)
    cur = conn.cursor()
    if fetchtype == datainfo.fetch_one:
        try:
            cur.execute(sql)
            data = cur.fetchone()
            list = data
   #         if data !='':
            print(list)
            cur.close()
  #          else:
 #               print("查询不到结果，请检查查询条件设置")
        except:
            conn.rollback()
        conn.close()
        return list[listindex]
    elif fetchtype == datainfo.fetch_all:
        try:
            cur.execute(sql)
            data = cur.fetchall()
            print(data)
            list = []
           # if data != '':
            for row in data:
                for i in row:
                    list.append(i)
                    cur.close()
          #  else:
         #      print("查询不到结果，请检查查询条件设置")
        except:
            conn.rollback()
        conn.close()
        return list[listindex]
    else:
        print("请输入正确的参数")


def deletesql(db_name,sql):
    conn = connectsql(db_name)
    cur = conn.cursor()
    try:
        cur.execute(sql)
        cur.close()
        conn.commit()
    except:
        conn.rollback()
    conn.close()

if __name__ == '__main__':
    projectname = input("请输入产品名称：")

    datetime1 = createdate('2018-2-28',"add",0,"date")

    datetime2 = '%'+datetime1
    SQL1 = '''UPDATE  xboss_investment_package_project SET contract_create_at=\'%s\' WHERE project_name like \'%s\'''' % (datetime1, '%'+projectname)
    SQL2 = '''select *  from xboss_investment_package_project  WHERE project_name LIKE \'%s\'  ''' % (projectname)

    print(SQL1)
    print(SQL2)
    # #updatesql(datainfo.xboss_db_name,SQL1)
    # updatesql(datainfo.xboss_db_name,SQL1)
    # data1 = selectsql(datainfo.xboss_db_name, SQL2,datainfo.fetch_one,0)
    # print(data1)
    # r = requests.get("https://dep.jbw666.com/console/command:Contracts")
    # data2 = selectsql(datainfo.xboss_db_name, SQL2,datainfo.fetch_all ,52)
    # print(data2)
