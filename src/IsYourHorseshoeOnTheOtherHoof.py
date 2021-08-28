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

class IsYourHorseshoeOnTheOtherHoof:
    def solve(self, s):
        a = []
        for i in s:
            if i not in a:
                a.append(i)
        print(4-len(a))

if __name__ == "__main__":
    s = Input.inlt()
    isYourHorseshoeOnTheOtherHoof = IsYourHorseshoeOnTheOtherHoof()
    isYourHorseshoeOnTheOtherHoof.solve(s)
