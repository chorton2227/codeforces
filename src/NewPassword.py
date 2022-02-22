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

class NewPassword:
    def solve(self, n, k):
        chars = "abcdefghijklmnopqrstuvwxyz"
        password = ""

        charIndex = 0
        for i in range(n):
            if (charIndex % k == 0):
                charIndex = 0
            password += chars[charIndex]
            charIndex += 1
        
        print(password)

if __name__ == "__main__":
    n, k = Input.invr()
    newPassword = NewPassword()
    newPassword.solve(n, k)
