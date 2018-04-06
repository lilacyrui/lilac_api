import datetime
import time
from jbhautotest.autotest.Data.basicdate  import  basicconfig

#创建时间
# 参数：开始时间，创建类型（加、减），时间间隔
def createdate(start_date,createtype ,dur_day, datetype):
    #将输入的开始时间格式转换 时间格式为 Y-M-D
    s_date = datetime.datetime.strptime(start_date,basicconfig.dateformat)
    #在开始时间上+ 时间间隔
    if createtype == basicconfig.date_add_type:
        date = (s_date + datetime.timedelta(days=dur_day)).strftime(basicconfig.dateformat)
        #返回生成日期+当前时间
        if datetype == 'date':
            return date
        elif datetype == 'datetime' :
            return date +' '+ basicconfig.now_time
    #在开始时间上-时间间隔
    elif createtype == basicconfig.date_min_type:
        date= (s_date - datetime.timedelta(days=dur_day)).strftime(basicconfig.dateformat)
        # 返回生成日期+当前时间
        if datetype == basicconfig.datetype_date:
            return date
        elif datetype == basicconfig.datetype_time :
            return date +' '+ basicconfig.now_time
    else:
        print("请输入正确的时间参数")

if __name__ == '__main__':
    date1 = createdate(basicconfig.now_date,basicconfig.date_add_type ,11,"date")
    print(datetime.datetime.now())
    datet2 = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
    date3 = createdate("2018-02-09",basicconfig.date_min_type ,3,"datetime")
    print(datet2)
    print(date1)
    print(date3)