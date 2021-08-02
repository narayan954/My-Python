from collections import deque

def check(ls):
    while True:
        big = ls.popleft() if ls[0]>ls[-1] else ls.pop()
        if not ls:
            return 'Yes'
        if big<ls[0] or big<ls[-1]:
            return 'No'

for _ in range(int(input())):
    a = int(input())
    ls = deque(map(int,input().split()))
    print(check(ls))
