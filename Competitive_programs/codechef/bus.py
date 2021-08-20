for _ in range(int(input())):
    n,m,q = map(int, input().split())
    ls = []
    flag = 1
    for _ in range(q):
        ch,i = input().split()
        if ch == '+':
            ls.append(i)
        else:
            if i in ls:
                ls.remove(i)
            else:
                flag = 0
        if len(ls)>m:
                flag = 0
          
    print('Consistent' if flag else 'Inconsistent')
