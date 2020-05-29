"""
SMTP（简单邮件传输协议），SMTP也是一个建立在TCP（传输控制协议）提供的可靠数据传输服务的基础上的应用级协议
它规定了邮件的发送者如何跟发送邮件的服务器进行通信的细节，而Python中的 smtplib 模块将这些操作简化成了几个简单的函数
"""

# 用Python发送邮件

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


def main():
    # 邮件发送者和接收者
    sender = "729461836@qq.com"
    receiver = "2418490593@qq.com"

    message = MIMEText("Hello World via Python SMTP Program !", "plain", "utf-8")
    message['From'] = Header('刘尚远', 'utf-8')
    message['To'] = Header('Bobby', 'utf-8')
    message['Subject'] = Header('邮件通讯示例', 'utf-8')
    smtper = SMTP('smtp.qq.com')

    # 登录账号，输入邮箱和授权码的base64编码
    smtper.login(sender, 'lffykfenzordbehh')
    smtper.sendmail(sender, receiver, message.as_string())
    print('邮件发送完成!')


if __name__ == '__main__':
    main()
