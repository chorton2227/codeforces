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

class Team:
    def solve(self, problem_sets):
        unsure = 0
        sure = 0
        for problems in problem_sets:
            unsure = 0
            for i in range(3):
                if problems[i] == 0:
                    unsure += 1
            if unsure < 2:
                sure += 1
        print(sure)


if __name__ == "__main__":
    n = Input.inp()
    problem_sets = []
    for i in range(n):
        problem_sets.append(Input.inlt())
    team = Team()
    team.solve(problem_sets)
