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

class StonesOnTheTable:
    def solve(self, n, stones):
        removes = 0
        pStone = None
        for i in range(n):
            if stones[i] == pStone:
                removes += 1
            pStone = stones[i]
        print(removes)

if __name__ == "__main__":
    n = Input.inp()
    stones = Input.insr()
    stonesOnTheTable = StonesOnTheTable()
    stonesOnTheTable.solve(n, stones)
