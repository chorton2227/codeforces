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

class ShaassAndOskols:
    def solve(self, n, a, m, shots):
        for shot in shots:
            x = shot[0]-1
            y = shot[1]
            left = y-1
            right = a[x]-y

            if x > 0:
                a[x-1] += left
            if x < len(a) - 1:
                a[x+1] += right
            a[x] = 0
        for i in a:
            print(i)

if __name__ == "__main__":
    n = Input.inp()
    a = Input.inlt()
    m = Input.inp()
    shots = []
    for i in range(m):
        shots.append(Input.inlt())
    shaassAndOskols = ShaassAndOskols()
    shaassAndOskols.solve(n, a, m, shots)
