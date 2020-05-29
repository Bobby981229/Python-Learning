"""
多线程 - 锁
可以通过“锁”来保护“临界资源”，只有获得“锁”的线程才能访问“临界资源”
而其他没有得到“锁”的线程只能被阻塞起来，直到获得“锁”的线程释放了“锁”
其他线程才有机会获得“锁”，进而访问被保护的“临界资源”
"""

from threading import Thread, Lock
from time import time, sleep


class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        self._lock.acquire()  # 先获取锁才能执行后续的代码
        try:
            new_balance = self._balance + money  # 计算存款后的余额
            sleep(0.01)  # 模拟受理存款业务需要0.01秒的时间
            self._balance = new_balance

        finally:
            # 在finally中执行释放锁的操作保证正常异常锁都能释放
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    for i in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("账户的余额为: $%d" % account.balance)


if __name__ == "__main__":
    main()
