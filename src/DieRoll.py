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

class DieRoll:
    def solve(self, y, w):
        m = max(y, w)
        den = 6
        num = den-m+1
        for i in range(2, den):
            if den % i == 0 and num % i == 0:
                den //= i
                num //= i
        print("%d/%d" % (num, den))

if __name__ == "__main__":
    y, w = Input.invr()
    dieRoll = DieRoll()
    dieRoll.solve(y, w)
