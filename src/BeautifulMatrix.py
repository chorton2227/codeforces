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

class BeautifulMatrix:
    def solve(self, matrix):
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == 1:
                    moves = abs(i - 2) + abs(j - 2)
                    print(moves)

if __name__ == "__main__":
    matrix = []
    for i in range(5):
        matrix.append(Input.inlt())
    beautifulMatrix = BeautifulMatrix()
    beautifulMatrix.solve(matrix)
