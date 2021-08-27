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
        s = input()
        return(list(s[:len(s) - 1]))

    """ Integer variable inputs """
    @staticmethod
    def invr():
        return(map(int, input().split()))

class VanyaAndFence:
    def solve(self, n, h, heights):
        width = 0
        for height in heights:
            if height > h: width += 2
            else: width += 1
        return width

if __name__ == "__main__":
    n, h = Input.invr()
    heights = Input.inlt()
    vanyaAndFence = VanyaAndFence()
    print(vanyaAndFence.solve(n, h, heights))
