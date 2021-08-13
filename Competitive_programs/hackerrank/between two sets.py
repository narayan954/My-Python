#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce
#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    lcm_a = reduce(lambda x,y: x*y//math.gcd(x,y), a)
    gcd_b = reduce(math.gcd, b)
    return sum(1 for x in range(lcm_a,gcd_b+1,lcm_a) if gcd_b%x==0)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
