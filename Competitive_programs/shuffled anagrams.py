import random
import math

for _ in range(int(input())):
    s = input().strip()

    for i in range(math.factorial(len(s))):
        temp = list(s)
        random.shuffle(temp)
        temp = ''.join(temp)
        flag = 1
        for i in range(len(s)):
            if s[i] == temp[i]:
                flag = 0
        if flag:
            print(temp)
            break
    if not flag:
        print('IMPOSSIBLE')
