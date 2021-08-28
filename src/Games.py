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

class Games:
    def solve(self, n, team_colors):
        numGames = n*(n-1)
        hostInGuest = 0
        for i in range(n):
            for j in range(i, n):
                if team_colors[i][0] == team_colors[j][1]:
                    hostInGuest += 1
                if team_colors[i][1] == team_colors[j][0]:
                    hostInGuest += 1
        print(hostInGuest)

if __name__ == "__main__":
    n = Input.inp()
    team_colors = []
    for i in range(n):
        team_colors.append(Input.inlt())
    games = Games()
    games.solve(n, team_colors)
