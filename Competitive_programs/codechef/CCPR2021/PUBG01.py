n = int(input())
prize = int(input())
expense = 0
for i in range(n):
    expense += sum(map(int,input().split()))
print((prize - expense)//n if expense<prize else 0)
