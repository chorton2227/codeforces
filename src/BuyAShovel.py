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

class BuyAShovel:
    def solve(self, k, r):
        buy = 1
        while True:
            cal = buy * k % 10
            if cal == r or cal == 0: break
            buy += 1
        print(buy)

if __name__ == "__main__":
    k, r = Input.inlt()
    buyAShovel = BuyAShovel()
    buyAShovel.solve(k, r)
