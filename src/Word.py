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

class Word:
    def solve(self, s):
        upCount = 0
        lwCount = 0
        for c in s:
            if c.isupper(): upCount += 1
            elif c.islower(): lwCount += 1
        out = "".join(s)
        if upCount > lwCount:
            print(out.upper())
        else:
            print(out.lower())

if __name__ == "__main__":
    s = Input.insr()
    word = Word()
    word.solve(s)
