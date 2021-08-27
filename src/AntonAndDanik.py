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

class AntonAndDanik:
    def solve(self, n, s):
        anton = 0
        danik = 0
        for i in range(n):
            if s[i] == 'A':
                anton += 1
            elif s[i] == 'D':
                danik += 1

        if anton > danik:
            print("Anton")
        elif danik > anton:
            print("Danik")
        else:
            print("Friendship")

if __name__ == "__main__":
    n = Input.inp()
    s = Input.insr()
    antonAndDanik = AntonAndDanik()
    antonAndDanik.solve(n, s)
