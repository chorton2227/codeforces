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

class TeamOlympiad:
    def solve(self, n, talents):
        talentsLen = len(talents)
        talentMap = [1, 2, 3]
        talentCount = []
        talentCursor = {}
        w = []

        for item in talentMap:
            talentCount.append(talents.count(item))

        for i in range(min(talentCount)):
            team = []
            for item in talentMap:
                cursor = 0
                if item in talentCursor.keys():
                    cursor = talentCursor[item]
                talents.reverse()
                index = talents.index(item, cursor)
                member = talentsLen - index - 1
                talents.reverse()
                talentCursor[item] = index + 1
                team.append(member + 1)
            w.append(team)

        print(len(w))
        for team in w:
           print(' '.join(map(str, team)))

if __name__ == "__main__":
    n = Input.inp()
    talents = Input.inlt()
    teamOlympiad = TeamOlympiad()
    teamOlympiad.solve(n, talents)
