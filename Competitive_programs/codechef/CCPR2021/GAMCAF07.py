# Codechef Campus code august -> Gaming cafe

def findComputers(arr, dep, n):
    arr.sort()
    dep.sort()

    # computers_needed indicates
    # number of computers
    # needed at a time
    computers_needed = 1
    result = 1
    i = 1
    j = 0

    # Similar to merge in
    # merge sort to process
    # all events in sorted order
    while i < n and j < n:

        # If next event in sorted
        # order is arrival,
        # increment count of
        # computers needed
        if arr[i] <= dep[j]:
            computers_needed += 1
            i += 1

        # Else decrement count
        # of computers needed
        else:
            computers_needed -= 1
            j += 1

        # Update result if needed
        if computers_needed > result:
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
