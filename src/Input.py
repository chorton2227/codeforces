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
