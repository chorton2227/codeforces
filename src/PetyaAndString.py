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

class PetyaAndStrings:
    def solve(self, a, b):
        a = a.lower()
        b = b.lower()
        
        if a > b: print(1)
        elif b > a: print(-1)
        else: print(0)

if __name__ == "__main__":
    a = Input.ins()
    b = Input.ins()
    petyaAndStrings = PetyaAndStrings()
    petyaAndStrings.solve(a, b)
