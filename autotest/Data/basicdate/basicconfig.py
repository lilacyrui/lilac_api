#coding = utf-8
import time
import datetime
#�����driver
driver_name = "chrome"

# ʱ����
dateformat = '%Y-%m-%d'
now = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
now_date = datetime.datetime.now().strftime("%Y-%m-%d")
now_time = datetime.datetime.now().strftime('%H:%M:%S')
date_add_type = 'add'
date_min_type = 'minus'
datetype_date = 'date'
datetype_time = 'datetime'

# ��ַ��
#��ǰbase_path
base_path = 'E:\\����\\python�Զ���\\jbhautotest\\jbhautotest\\autotest'
#�����ŵ�ַ
result_path= '\\Test_Result\\'
#����Ŀ¼����
report_dir = 'report\\'
# ��־Ŀ¼����
log_dir = 'log\\'
#��ͼĿ¼��ַ
screen_dir = 'screenshot\\'

#������������
case_path = '\\Test_Case\\'
case_pattern = 'Test_*.py'

#�����ʼ���Ϣ
smtServer = 'smtp.qq.com'
sender = '43734971@qq.com'
password = 'zrvliytvtylacaeg'
receiver = "43734971@qq.com"
subject = 'С���Զ�������'
From = 'С���Զ���'
To = 'С������'


#���Ա��涨��
report_title= '�����������Ա���'
report_description = '��������ִ�����:'

