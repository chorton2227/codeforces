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

class PoliceRecruits:
    def solve(self, n, events):
        count = 0
        untreated_crimes = 0
        for event in events:
            if event == -1 and count < 1:
                untreated_crimes += 1
            elif event == -1 and count > 0:
                count += event
            elif event > 0:
                count += event
        print(untreated_crimes)

if __name__ == "__main__":
    n = Input.inp()
    events = Input.inlt()
    policeRecruits = PoliceRecruits()
    policeRecruits.solve(n, events)
