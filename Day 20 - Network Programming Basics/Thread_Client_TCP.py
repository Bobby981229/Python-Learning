"""
客户端
"""

import socket  # 导入 socket 模块

s = socket.socket()  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 42683  # 设置端口好

s.connect((host, port))
print(s.recv(1024).decode())
s.close()

# from socket import socket
# from json import loads
# from base64 import b64decode
#
#
# def main():
#     client = socket()
#     client.connect(('192.168.1.106', 51652))
#     # 定义一个保存二进制数据的对象
#     in_data = bytes()
#     # 由于不知道服务器发送的数据有多大每次接收1024字节
#     data = client.recv(1024)
#     while data:
#         # 将收到的数据拼接起来
#         in_data += data
#         data = client.recv(1024)
#     # 将收到的二进制数据解码成JSON字符串并转换成字典
#     # loads函数的作用就是将JSON字符串转成字典对象
#     my_dict = loads(in_data.decode('utf-8'))
#     filename = my_dict['filename']
#     filedata = my_dict['filedata'].encode('utf-8')
#     with open('C:/Users/72946/Pictures/Camera Roll/QQ.jpg/' + filename, 'wb') as f:
#         # 将base64格式的数据解码成二进制数据并写入文件
#         f.write(b64decode(filedata))
#     print('图片已保存.')
#
#
# if __name__ == '__main__':
#     main()
