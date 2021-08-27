#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    n = arr[-1]
    for i in range(1,len(arr)):
        if arr[-i-1] > n:
            arr[-i] = arr[-i-1]
            print(' '.join(map(str,arr)))
        else:
            arr[-i] = n
            print(' '.join(map(str,arr)))
            break
    if arr[0]>n:
        arr[0] = n
        print(*arr)
        
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
