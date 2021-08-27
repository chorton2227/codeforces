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

class Magnets:
    def solve(self, n, m):
        g = 0
        pm = None
        for i in range(n):
            if pm is None:
                g += 1
            elif pm[1] == m[i][0]:
                g += 1
            pm = m[i]
        print(g)

if __name__ == "__main__":
    n = Input.inp()
    m = []
    for i in range(n):
        m.append(Input.insr())
    magnets = Magnets()
    magnets.solve(n, m)
