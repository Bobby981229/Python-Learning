"""
面向对象编程应用
"""

# 扑克游戏 - 简单起见，我们的扑克只有52张牌（没有大小王）
# 游戏需要将52张牌发到4个玩家的手上，每个玩家手上有13张牌
# 按照黑桃、红心、草花、方块的顺序和点数从小到大排列，暂时不实现其他的功能

"""
类和类之间的关系可以粗略的分为is-a关系（继承）、has-a关系（关联）和use-a关系（依赖）
很显然扑克和牌是has-a关系，因为一副扑克有（has-a）52张牌
玩家和牌之间不仅有关联关系还有依赖关系，因为玩家手上有（has-a）牌而且玩家使用了（use-a）牌
"""

# Python中没有声明枚举类型的关键字，但是可以通过继承enum模块的Enum类来创建枚举类型

from enum import Enum


class Suite(Enum):
    """花色(枚举)"""
    SPADE, HEART, CLUB, DIAMOND = range(4)


for i in Suite:
    print(f'{i}: {i.value}')
    print()


class Card:
    """牌类"""

    # 初始化
    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    # __repr__() 会返回和调用者有关的 “类名+object at+内存地址”信息
    def __repr__(self):
        suites = '♠♥♣♦'
        face = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        # 根据牌的花色和点数取到对应的字符
        return f'{suites[self.suite.value]} {face[self.face]}'


card1 = Card(Suite.SPADE, 5)
card2 = Card(Suite.HEART, 13)
print(card1, card2)    # ♠5 ♥K


import random


class Poker:
    """扑克"""

    def __init__(self):
        # 通过列表的生成式语法创建一个装52张牌的列表
        self.cards = [Card(suite, face) for suite in Suite
                      for face in range(1, 14)]
        # current属性表示发牌的位置
        self.current = 0

    def shuffle(self):
        """洗牌"""
        self.current = 0
        # 通过random模块的shuffle函数实现列表的随机乱序
        random.shuffle(self.cards)

    def deal(self):
        """发牌"""
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_next(self):
        """还有没有牌可以发"""
        return self.current < len(self.cards)


poker = Poker()
poker.shuffle()
print(poker.cards)


class Player:
    """玩家"""

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_one(self, card):
        """摸牌"""
        self.cards.append(card)

    def arrange(self):
        self.cards.sort()


poker = Poker()
poker.shuffle()
players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
for _ in range(13):
    for player in players:
        player.get_one(poker.deal())
for player in players:
    player.arrange()
    print(f'{player.name}: ', end='')
    print(player.cards)


class Card:
    """牌"""

    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        # 根据牌的花色和点数取到对应的字符
        return f'{suites[self.suite.value]}{faces[self.face]}'

    def __lt__(self, other):
        # 花色相同比较点数的大小
        if self.suite == other.suite:
            return self.face < other.face
        # 花色不同比较花色对应的值
        return self.suite.value < other.suite.value


