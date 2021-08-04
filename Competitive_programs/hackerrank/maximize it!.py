from itertools import product
k, m = map(int,input().split())
s = []
for i in range(k):
    ls = map(int,input().split()[1:])
    s.append(map(lambda x: x**2%m,ls))
print(max(map(lambda x: sum(x)%m, product(*s))))
