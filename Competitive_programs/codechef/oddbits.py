for _ in range(int(input())):
    n = int(input())
    alpha, omega = 1, 10**9


    def getk(x, bits):
        #print(x, bits)
        ans = 0
        for j in range(1, bits , 2):
            i = bits - j - 1
            #print(i)
            y = x // (2 ** i)
            ans += (y // 2) * (2 ** i)
            if y % 2:
                ans += x % (2 ** i)
        return ans


    def calc(x):
        ans = x
        for b in range(60):
            size = b + 1
            if x >= 2 ** size - 1:
                cnt = 2 ** b
                ans += (cnt // 2) * (b // 2)
            else:
                left = x - 2 ** b + 1
                if left <= 0: break
                bits = b
                ans += getk(left, bits)
                break
        return ans
    while alpha < omega:
        x = (alpha + omega) // 2
        if calc(x) >= n:
            omega = x
        else:
            alpha=  x + 1
    print(alpha)
