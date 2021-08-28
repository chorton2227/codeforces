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

class ColorfulStonesSimple:
    def solve(self, s, t):
        pos = 0
        for c in t:
            if s[pos] == c: pos += 1
        print(pos+1)

if __name__ == "__main__":
    s = Input.insr()
    t = Input.insr()
    colorfulStonesSimple = ColorfulStonesSimple()
    colorfulStonesSimple.solve(s, t)
