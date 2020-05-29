import random

result = random.randint(1, 100)
count = 0

while True:
    count += 1
    answer = int(input('请输入数字: '))
    if answer > result:
        print("小一点")
    elif answer < result:
        print("大一点")
    else:
        print("猜对了")
        break  # 终止循环
print("\n您一共猜了%d次, 最终答案为%d" % (count, result))
