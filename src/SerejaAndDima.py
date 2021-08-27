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

class SerejaAndDima:
    def solve(self, n, cards):
        sereja = 0
        dima = 0

        turn = 0
        left = 0
        right = n-1

        while turn < n:
            card = 0
            if cards[left] > cards[right]:
                card = cards[left] 
                left += 1
            else:
                card = cards[right]
                right -= 1

            if turn % 2 == 0:
                sereja += card
            else:
                dima += card

            turn += 1

        print(sereja, dima)

if __name__ == "__main__":
    n = Input.inp()
    cards = Input.inlt()
    serejaAndDima = SerejaAndDima()
    serejaAndDima.solve(n, cards)
