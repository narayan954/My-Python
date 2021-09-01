s = input().strip()
checker = input().strip().split()
ls = []
for i in range(len(s)):
    ls.append(s[i:] + s[:i])
for i in checker:
    if i in ls:
        print(i,end=' ')
