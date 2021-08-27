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

class BoyOrGirl:
    def solve(self, s):
        seen = []
        for c in s:
            if c not in seen:
                seen.append(c)

        if len(seen) % 2 == 0:
            print("CHAT WITH HER!")
        else:
            print("IGNORE HIM!")

if __name__ == "__main__":
    s = Input.insr()
    boyOrGirl = BoyOrGirl()
    boyOrGirl.solve(s)
