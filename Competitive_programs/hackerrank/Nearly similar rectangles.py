#TLE
"""
def nearlySimilarRectangles(sides):
    c = 0
    for i in range(len(sides) - 1):
        for j in range(i + 1, len(sides)):
            if sides[i][0] * sides[j][1] == sides[i][1] * sides[j][0]:
                c += 1
    return c
"""
#TLE
"""
def nearlySimilarRectangles(sides):
    ls = []
    c = 0
    for i in range(len(sides)):
        ls.append(sides[i][0] / sides[i][1])
    for i in range(len(ls) - 1):
        for j in range(i + 1, len(ls)):
            if ls[i] == ls[j]:
                c += 1
    return c
"""
def nearlySimilarRectangles(sides):
    totalSides = len(sides)
    freq = {}
    ns = 0
    for side in sides:
        ratio = side[0]/side[1]
        if freq.get(ratio) is None:
            freq[ratio] = 1
        else:
            freq[ratio] += 1
    for k,v in freq.items():
        if v!=1:
            ns += int(math.factorial(v)/(math.factorial(v-2)*math.factorial(2)))
    return ns


if __name__ == '__main__':

    sides_rows = int(input().strip())
    sides_columns = int(input().strip())

    sides = []

    for _ in range(sides_rows):
        sides.append(list(map(int, input().rstrip().split())))

    result = nearlySimilarRectangles(sides)

    print(str(result) + '\n')
