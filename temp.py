#given an array a[1],a[2],a[3],a[4]...a[n] , return an array such that element at a[i] is product of every element but the one at a[i] originally ...
# constraint : no extra array other than modification one and original

ls = [1, 2, 3, 4, 5]
temp = [1]

n = len(ls)
for i in range(1, n):
    x = temp[i - 1] * ls[i - 1]
    temp.append(x)

las_el = ls[n - 1]
ls[n - 1] = temp[n - 1]
for i in range(n - 2, -1, -1):
    cur_el = ls[i]
    ls[i] = temp[i] * las_el
    las_el *= cur_el
print(temp)
print(ls)

'''
#just wanna think if this wont do
def red(lst):
    prod = 1
    for i in lst:
        prod *= i
    return prod


ls = [1, 2, 3, 4, 5]
ls_1 = []

for k in range(len(ls)):
    x = red(ls[i] for i in range(len(ls)) if ls[i] != ls[k])
    ls_1.append(x)

print(ls_1)
'''
