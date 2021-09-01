def findComputers(arr, dep, n):
    arr.sort()
    dep.sort()
    
    computers_needed = 1
    result = 1
    i = 1
    j = 0

    while (i < n and j < n):
        if (arr[i] <= dep[j]):
            computers_needed += 1
            i += 1
            
        elif (arr[i] > dep[j]):
            computers_needed -= 1
            j += 1
            
        if (computers_needed > result):
            result = computers_needed

    return result


# Driver code
n = int(input())
arr = []
dep = []
for _ in range(n):
    a, d = map(int, input().split())
    arr.append(a)
    dep.append(d)

print(findComputers(arr, dep, n))
