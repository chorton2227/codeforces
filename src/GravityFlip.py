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

class GravityFlip:
    def solve(self, n, a):
        a.sort()
        sa = [str(e) for e in a]
        print(" ".join(sa))

if __name__ == "__main__":
    n = Input.inp()
    a = Input.inlt()
    gravityFlip = GravityFlip()
    gravityFlip.solve(n, a)
