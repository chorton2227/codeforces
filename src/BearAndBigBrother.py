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

    """ List of characters """
    @staticmethod
    def insr():
        return(list(input()))

    """ Integer variable inputs """
    @staticmethod
    def invr():
        return(map(int, input().split()))

class BearAndBigBrother:
    def solve(self, a, b):
        i = 0
        while True:
            i += 1
            a *= 3
            b *= 2
            if a > b:
                print(i)
                return


if __name__ == "__main__":
    a, b = Input.invr()
    bearAndBigBrother = BearAndBigBrother()
    bearAndBigBrother.solve(a, b)
