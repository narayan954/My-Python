def fun(arr, index):
    if index > 9:
        print(arr)
        return
    for i in range(10):
        arr[index] = i
        fun(arr, index + 1)


arr = [0] * 10

for i in range(6, 10):
    arr[0] = i
    fun(arr, 1)
