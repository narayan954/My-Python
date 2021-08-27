#!/bin/python3

import math
import os
import random
import re
import sys

def jumpingOnClouds(c, k):
    i = k % n                  # initial jump from zero
    count = c[i] * 2 + 1       # initial loss count
    while i != 0:               
        i = (i+k)%n            # for that round/circle effect
        count += c[i] * 2 + 1  # loss count at every step
    return 100 - count         # returning the estimate
      

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
