def find_dis(l, m):
  return abs(m-y) + abs(x-l)

x, y = map(int, input().split())
l, m = map(int, input().split())
closest_co = [l, m]
closest_dis = find_dis(l, m)

while True:
    try:
        temp_l, temp_m = map(int, input().split())
        temp_dis = find_dis(temp_l,temp_m)
        if temp_dis < closest_dis:
          closest_dis = temp_dis
          closest_co = [temp_l, temp_m]
    except:
        break

for i in closest_co:
    print(i, end = ' ')
