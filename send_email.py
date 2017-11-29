    import os
    import sys
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    
    mail_host = ""    # SMTP服务器 如：smtp.126.com
    mail_user = ""    # 用户名
    mail_pass = ""    # 授权密码，非登录密码
    sender = ''       # 发件人邮箱(最好写全, 不然会失败)
    receivers = ['']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    
    def sendEmail(title, content_lst):
        message = MIMEMultipart()
        message['From'] = "{}".format(sender)
        message['To'] = ",".join(receivers)
        message['Subject'] = title
        message.attach(MIMEText(str(content_lst))) # 邮件正文内容
        #构造附件1，传送当前目录下的 data.txt 文件
        # att1 = MIMEText(open(file_name, 'r').read(), 'base64', 'utf-8')
        # att1['Content-Type'] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        # att1['Content-Disposition'] = 'attachment; filename="data.txt"'
        # message.attach(att1)
        try:
            smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
            smtpObj.login(mail_user, mail_pass)  # 登录验证
            smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
            print("mail has been send successfully.")
        except smtplib.SMTPException as e:
            print(e)
