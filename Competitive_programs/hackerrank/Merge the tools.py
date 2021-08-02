def merge_the_tools(string, k):
    temp = []
    ls_c = 0
    for item in string:
        ls_c += 1
        if item not in temp:
            temp.append(item)
        if ls_c == k:
            print(''.join(temp))
            temp = []
            ls_c = 0

