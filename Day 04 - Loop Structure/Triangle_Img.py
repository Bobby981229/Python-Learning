"""
打印如下所示的三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********
"""

# 图01
rows = int(input('请输入行数: '))
for i in range(rows):
    for j in range(i + 1):
        print('*', end='')
    print()

# 图02
rows = int(input('请输入行数: '))
for i in range(rows):
    for j in range(rows):
        if j < rows - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

# 图03
rows = int(input('请输入行数: '))
for i in range(rows):
    for j in range(rows - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        print('*', end='')
    print()
