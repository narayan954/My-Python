def count(ar):
    out = [0] * 100
    for i in ar:
        out[i] += 1

    return out

def printOrdered(arr):
    for i in range(0, 100):
        for j in range(0, arr[i]):
            print(i, end=' ')


m = input()
ar = [int(i) for i in input().strip().split()]
printOrdered(count(ar))
