#!/bin/python3

import statistics as stat


#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    ls = []
    for i in range(n):
        ls.extend([values[i]] * freqs[i])
    ls.sort()
    left = ls[:len(ls) // 2]
    if len(ls)%2 == 0:
        right =ls[len(ls)//2:]
    else:
        right =ls[len(ls)//2+1:]
    print(float(stat.median(right) - stat.median(left)))


if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
