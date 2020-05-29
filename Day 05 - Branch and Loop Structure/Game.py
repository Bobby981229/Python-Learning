"""
Craps赌博游戏
我们设定玩家开始游戏时有1000元的赌注
游戏结束的条件是玩家输光所有的赌注

该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏；
玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；
其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。
"""
from random import randint

money = 1000
while money > 0:
    print('你的总资产为:', money)
    needs_go_on = False

    # 下注金额必须在当前资产以内，否则循环
    while True:
        debt = int(input('请下注: '))
        if 0 < debt <= money:
            break

    first = randint(1, 6) + randint(1, 6)  # 随机两粒骰子点数之和
    print('玩家摇出了%d点' % first)  # 显示当前骰子点数

    if first == 7 or first == 11:  # 判断点数之和是否为7或11, 来判断玩家是否胜利
        print('玩家胜!')
        money += debt  # 总资产 = 原资产 + 赌注
    elif first == 2 or first == 3 or first == 12:  # 若点数之和为2, 3或12, 则庄家胜
        print('庄家胜!')  # 总资产 = 原资产 - 赌注
        money -= debt
    # 如果都不是, 则进入第二轮
    else:
        needs_go_on = True
    while needs_go_on:
        needs_go_on = False
        current = randint(1, 6) + randint(1, 6)  # 随机两粒骰子点数之和
        print('玩家摇出了%d点' % current)
        if current == 7:
            print('庄家胜')  # 总资产 = 原资产 - 赌注
            money -= debt
        elif current == first:
            print('玩家胜')  # 总资产 = 原资产 + 赌注
            money += debt
        else:
            needs_go_on = True
print('你破产了, 游戏结束!')