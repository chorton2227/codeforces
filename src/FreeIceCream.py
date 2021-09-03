#!/usr/bin/python3

import sys

class Input:
    """ Integer inputs """
    @staticmethod
    def inp():
        return(int(input()))

    """ List inputs """
    @staticmethod
    def inlt():
        return(list(map(int, input().split())))

    """ String inputs """
    @staticmethod
    def ins():
        return(input())

    """ List of characters """
    @staticmethod
    def insr():
        return(list(input()))

    """ Integer variable inputs """
    @staticmethod
    def invr():
        return(map(int, input().split()))

class FreeIceCream:
    def solve(self, n, x, queue):
        gerda = 0
        for item in queue:
            a = item.split(' ')
            op = a[0]
            num = int(a[1])
            if op == '+':
                x += num
            else:
                if x >= num:
                    x -= num
                else:
                    gerda += 1
        print(x, gerda)

if __name__ == "__main__":
    n, x = Input.invr()
    queue = []
    for i in range(n):
        queue.append(Input.ins())
    freeIceCream = FreeIceCream()
    freeIceCream.solve(n, x, queue)
