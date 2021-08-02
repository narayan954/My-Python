for _ in range(int(input())):
    n, k = map(int,input().split())
    max_shift = pow(2, n-1)
    temp = pow(2,n)-1
    if k > max_shift:
        sum = 2*temp*max_shift
    else:
        sum = 2*temp*k 
    print(sum)
