#!/bin/python3

import os
import sys


#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    ls = []
    for kb_price in keyboards:
        for d_price in drives:
            ls.append(kb_price + d_price)
    ls.sort()
    if ls[0] > b:
        return -1
    else:
        for i in range(len(ls)):
            if ls[i] > b:
                return ls[i - 1]


if __name__ == '__main__':

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    print(str(moneySpent) + '\n')

