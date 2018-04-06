#coding = utf-8
import time
import datetime
#浏览器driver
driver_name = "chrome"

# 时间类
dateformat = '%Y-%m-%d'
now = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
now_date = datetime.datetime.now().strftime("%Y-%m-%d")
now_time = datetime.datetime.now().strftime('%H:%M:%S')
date_add_type = 'add'
date_min_type = 'minus'
datetype_date = 'date'
datetype_time = 'datetime'

# 地址类
#当前base_path
base_path = 'E:\\测试\\python自动化\\jbhautotest\\jbhautotest\\autotest'
#结果存放地址
result_path= '\\Test_Result\\'
#报告目录名称
report_dir = 'report\\'
# 日志目录名称
log_dir = 'log\\'
#截图目录地址
screen_dir = 'screenshot\\'

#测试用例搜索
case_path = '\\Test_Case\\'
case_pattern = 'Test_*.py'

#发送邮件信息
smtServer = 'smtp.qq.com'
sender = '43734971@qq.com'
password = 'zrvliytvtylacaeg'
receiver = "43734971@qq.com"
subject = '小贷自动化测试'
From = '小贷自动化'
To = '小贷测试'


#测试报告定义
report_title= '海航白条测试报告'
report_description = '测试用例执行情况:'

