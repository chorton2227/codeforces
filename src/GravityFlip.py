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

class GravityFlip:
    def solve(self, n, a):
        box = []
        for i in range(n):
            col = []
            numRows = max(a)
            for j in range(numRows):
                cube = 0
                if a[i] > j:
                    cube = 1
                col.append(cube)
            box.append(col)

        changed = True
        while changed:
            changed = False
            for i in reversed(range(len(box))):
                for j in range(len(box[i])):
                    if i > 0 and box[i][j] == 0 and box[i-1][j] == 1:
                        changed = True
                        box[i][j] = box[i-1][j]
                        box[i-1][j] = 0

        out = ""
        for i in range(len(box)):
            out += str(sum(box[i])) + " "
        print(out)

if __name__ == "__main__":
    n = Input.inp()
    a = Input.inlt()
    gravityFlip = GravityFlip()
    gravityFlip.solve(n, a)
