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

class NightAtTheMuseum:
    def solve(self, s):
        chars = 'abcdefghijklmnopqrstuvwxyz';
        moves = 0
        cursor = 0
        for c in s:
            new_cursor = chars.index(c)
            idx1 = abs(new_cursor - cursor)
            idx2 = abs(idx1 - len(chars))
            move = min(idx1, idx2)
            moves += move
            cursor = new_cursor
        print(moves)

if __name__ == "__main__":
    s = Input.ins()
    nightAtTheMuseum = NightAtTheMuseum()
    nightAtTheMuseum.solve(s)
