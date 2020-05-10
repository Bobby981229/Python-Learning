"""
平面上的点，计算到另一个点距离的方法
"""


class Point(object):
    """屏面上的点"""

    def __init__(self, x=0, y=0):
        """初始化方法
        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x = x
        self.y = y

    def distance(self, other):
        """计算与另一个点的距离
        :param other: 另一个点
        """
        dx = self.x - other.x
        dy = self.y - other.y
        dis = ((dx * dx) + (dy * dy)) ** 0.5  # C² = A² + B²
        return dis

    def __str__(self):
        return f'({self.x}, {self.y})'


p1 = Point(3, 5)
p2 = Point(6, 9)
print(p1, p2)
print('Distance:', p1.distance(p2))
