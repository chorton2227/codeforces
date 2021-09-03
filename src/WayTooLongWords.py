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

class WayTooLongWords:
    def solve(self, n, words):
        for word in words:
            if len(word) > 10:
                print("{0}{1}{2}".format(word[0], len(word) - 2, word[-1]))
            else:
                print(word)

if __name__ == "__main__":
    n = Input.inp()
    words = []
    for i in range(n):
        words.append(Input.ins())
    wayTooLongWords = WayTooLongWords()
    wayTooLongWords.solve(n, words)
