"""
发送带有附件的邮件
"""

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

import urllib


def main():
    # 创建一个带附件的邮件消息对象
    message = MIMEMultipart()

    # 创建文本内容
    text_content = MIMEText("Email Sent via Python_SMTP\n宋玉正秋悲，\n逐朵云如吐。\n千万朵莺羽，\n花残惜晚晖，\n官贫心甚安。 ", "plain", "utf-8")  # 邮件正文
    message['Subject'] = Header("Python Email Demo")  # 邮件主题
    message.attach(text_content)  # 将文本内容添加到邮件消息对象中

    # 读取文件并将文件作为附件
    with open('C:/Users/72946/Desktop/复习文档.doc', 'rb') as f:
        txt = MIMEText(f.read(), 'base64', 'utf-8')
        txt['Content-Type'] = 'application/msword'
        txt['Content-Disposition'] = 'attachment; filename=复习文档.doc'
        message.attach(txt)  # 添加到邮件消息对象中

    # 读取文件并将文件作为附件
    with open('C:/Users/72946/Desktop/XXX.jpg', 'rb') as f:
        png = MIMEText(f.read(), 'base64', 'utf-8')
        png['Content-Type'] = 'image/jpeg'
        png['Content-Disposition'] = 'attachment; filename=XXX.jpg'
        message.attach(png)  # 添加到邮件消息对象中

    # 创建SMTP对象
    smtper = SMTP('smtp.qq.com')
    # 开启安全连接
    # smtper.starttls()
    sender = "729461836@qq.com"
    receiver = ["437487797@qq.com"]
    # 登录到SMTP服务器
    # 请注意此处不是使用密码而是邮件客户端授权码进行登录
    # 对此有疑问的读者可以联系自己使用的邮件服务器客服
    smtper.login(sender, 'lffykfenzordbehh')
    # 发送邮件
    smtper.sendmail(sender, receiver, message.as_string())
    # 与邮件服务器断开连接
    smtper.quit()
    print('发送完成!')


if __name__ == '__main__':
    main()
