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

class HelpfulMaths:
    def solve(self, s):
        nums = s.split('+')
        nums.sort()
        print('+'.join(nums))

if __name__ == "__main__":
    s = Input.ins()
    helpfulMaths = HelpfulMaths()
    helpfulMaths.solve(s)
