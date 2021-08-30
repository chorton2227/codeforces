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

class Juicer:
    def solve(self, n, b, d, a):
        waste = 0
        emptied = 0
        for an in a:
            if an > b:
                continue
            waste += an
            if waste > d:
                waste = 0
                emptied += 1
        print(emptied)


if __name__ == "__main__":
    n, b, d = Input.invr()
    a = Input.inlt()
    juicer = Juicer()
    juicer.solve(n, b, d, a)
