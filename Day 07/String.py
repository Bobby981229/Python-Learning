"""
字符串
"""

s1 = 'hello, world!'
s2 = "hello, world!"

# 以三个双引号或单引号开头的字符串可以折行
s3 = """
hello, 
world!
"""
print(s1, s2, s3, end='')
print('\n******************************\n')

"""
换行
"""
s1 = '\'hello, world!\''  # \（反斜杠）表示转义
s2 = '\n\\hello, world!\\\n'  # \n 表示换行, \t 表示制表符
print(s1, s2, end='')
print('\n******************************\n')

"""
\141 八进制或者十六进制数来表示字符
"""
s1 = '\141\142\143\x61\x62\x63\n'  # \ 跟一个八进制或者十六进制数来表示字符
print(s1)
# \ 后面跟Unicode字符编码来表示字符
name = u'刘尚远'.encode('unicode-escape')  # 将字符转换为Unicode格式
name2 = '\u5218\u5c1a\u8fdc'  # 将Unicode转中文
print('姓名-Unicode:', name)
print('姓名-字符:', name2)
print('\n******************************\n')

# r在前面，则\不表示转义，显示引号内的所有内容
s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')
