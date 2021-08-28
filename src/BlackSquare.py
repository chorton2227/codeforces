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

class BlackSquare:
    def solve(self, a, s):
        calories = 0
        for c in s:
            if c == '1':
                calories += a[0]
            elif c == '2':
                calories += a[1]
            elif c == '3':
                calories += a[2]
            elif c == '4':
                calories += a[3]
        print(calories)

if __name__ == "__main__":
    a = Input.inlt()
    s = Input.insr()
    blackSquare = BlackSquare()
    blackSquare.solve(a, s)
