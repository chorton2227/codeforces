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

class AntonAndLetters:
    def solve(self, letters):
        if len(letters) <= 2:
            print(0)
            return
        distinct = []
        letters = letters[1:-1].split(', ')
        for letter in letters:
            if letter not in distinct:
                distinct.append(letter)
        print(len(distinct))

if __name__ == "__main__":
    letters = Input.ins();
    antonAndLetters = AntonAndLetters()
    antonAndLetters.solve(letters)
