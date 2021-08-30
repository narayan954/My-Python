t = int(input())
for j in range(1, t + 1):
    s = input()
    if len(s) == 1:
        print(f"Case #{j}:", 0)
        continue
    a = 26 * [0]
    x, y, h = 0, 0, 0
    for i in s:
        a[ord(i) - 65] += 1
        if i in 'AEIOU':
            x += 1
        else:
            y += 1
            if a[ord(i) - 65] > h:
                h = a[ord(i) - 65]
    if x <= y:
        print(f"Case #{j}:", y + 2 * (x - max(a[0], a[4], a[8], a[14], a[20])))
    else:
        print(f"Case #{j}:", x + 2 * (y - h))
