import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from jbhautotest.UIautotest.Data.basicdate import basicconfig


def Sendmail(file):

    #读取生成的最新的报告
    f = open(file,'rb')
    mailbody = f.read()
    f.close()

    #设置读取内容为邮件的正文
    content = MIMEText(mailbody,'html','utf-8')

    # 设置最新的报告为邮件的附件
    att = MIMEText(mailbody,'base64','utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename=report.html'

    # 设置邮件的发件人、收件人、主题
    msgRoot = MIMEMultipart('related')
    msgRoot['From']=Header(basicconfig.From, 'utf-8')
    msgRoot['To']=Header(basicconfig.To, 'utf-8')
    msgRoot['Subject'] = Header(basicconfig.subject, 'utf-8')

    # 添加邮件的正文和附件
    msgRoot.attach(content)
    msgRoot.attach(att)

    #连接邮件服务器
    server=smtplib.SMTP(basicconfig.smtServer, 25)
    server.set_debuglevel(1)
    server.starttls()

    #发件人登录邮箱
    server.login(basicconfig.sender, basicconfig.password)
    #发送邮件
    server.sendmail(basicconfig.sender, basicconfig.receiver.split(','), msgRoot.as_string())

    #取消连接邮件服务器
    server.quit()