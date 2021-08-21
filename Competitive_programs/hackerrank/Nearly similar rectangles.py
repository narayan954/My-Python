"""
def nearlySimilarRectangles(sides):
    c = 0
    for i in range(len(sides) - 1):
        for j in range(i + 1, len(sides)):
            if sides[i][0] * sides[j][1] == sides[i][1] * sides[j][0]:
                c += 1
    return c
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


if __name__ == '__main__':

    sides_rows = int(input().strip())
    sides_columns = int(input().strip())

    sides = []

    for _ in range(sides_rows):
        sides.append(list(map(int, input().rstrip().split())))

    result = nearlySimilarRectangles(sides)

    print(str(result) + '\n')
