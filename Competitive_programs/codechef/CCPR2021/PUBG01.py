players = int(input())
prize = int(input())
expense = 0
for i in range(players):
    expense += sum(map(int, input().split()))
print((prize - expense)//players if expense < prize else 0)
