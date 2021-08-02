# ------------------- fast io --------------------
import os
import sys
from io import BytesIO, IOBase

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0
    
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
    
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
    
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
    
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# ------------------- fast io --------------------
from math import ceil


def prod(a, mod=10 ** 9 + 7):
    ans = 1
    for each in a:
        ans = (ans * each) % mod
    return ans


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(a, b): return a * b // gcd(a, b)


def binary(x, length=16):
    y = bin(x)[2:]
    return y if len(y) >= length else "0" * (length - len(y)) + y


from bisect import bisect_left, bisect_right


class Result:
    def __init__(self, index, value):
        self.index = index
        self.value = value


class BinarySearch:
    def __init__(self):
        pass
    
    @staticmethod
    def greater_than(num: int, func, size: int = 1):
        """Searches for smallest element greater than num!"""
        if isinstance(func, list):
            index = bisect_right(func, num)
            if index == len(func):
                return Result(None, None)
            else:
                return Result(index, func[index])
        else:
            alpha, omega = 0, size - 1
            if func(omega) <= num:
                return Result(None, None)
            while alpha < omega:
                if func(alpha) > num:
                    return Result(alpha, func(alpha))
                if omega == alpha + 1:
                    return Result(omega, func(omega))
                mid = (alpha + omega) // 2
                if func(mid) > num:
                    omega = mid
                else:
                    alpha = mid
    
    @staticmethod
    def less_than(num: int, func, size: int = 1):
        """Searches for largest element less than num!"""
        if isinstance(func, list):
            index = bisect_left(func, num) - 1
            if index == -1:
                return Result(None, None)
            else:
                return Result(index, func[index])
        else:
            alpha, omega = 0, size - 1
            if func(alpha) >= num:
                return Result(None, None)
            while alpha < omega:
                if func(omega) < num:
                    return Result(omega, func(omega))
                if omega == alpha + 1:
                    return Result(alpha, func(alpha))
                mid = (alpha + omega) // 2
                if func(mid) < num:
                    alpha = mid
                else:
                    omega = mid

bs = BinarySearch()

from math import inf, log2


class SegmentTree:
    def __init__(self, array, func=max):
        self.n = len(array)
        self.size = 2 ** (int(log2(self.n - 1)) + 1) if self.n != 1 else 1
        self.func = func
        self.default = 0 if self.func != min else inf
        self.data = [self.default] * (2 * self.size)
        self.process(array)
    
    def process(self, array):
        self.data[self.size: self.size + self.n] = array
        for i in range(self.size - 1, -1, -1):
            self.data[i] = self.func(self.data[2 * i], self.data[2 * i + 1])
    
    def query(self, alpha, omega):
        """Returns the result of function over the range (inclusive)!"""
        if alpha == omega:
            return self.data[alpha + self.size]
        res = self.default
        alpha += self.size
        omega += self.size + 1
        while alpha < omega:
            if alpha & 1:
                res = self.func(res, self.data[alpha])
                alpha += 1
            if omega & 1:
                omega -= 1
                res = self.func(res, self.data[omega])
            alpha >>= 1
            omega >>= 1
        return res
    
    def update(self, index, value):
        """Updates the element at index to given value!"""
        index += self.size
        self.data[index] = value
        index >>= 1
        while index:
            self.data[index] = self.func(self.data[2 * index], self.data[2 * index + 1])
            index >>= 1


for _ in range(int(input()) if True else 1):
    #n = int(input())
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    x = []
    for i in range(n):
        x += [[a[i], b[i]]]
    x = sorted(x)

    tastes = [k[1] for k in x]
    prices = [k[0] for k in x]
    mx = 0
    cc = []
    for i in range(n):
        if tastes[i] >= mx:
            mx = max(mx, tastes[i])
            cc += [i]

    ans = 0
    for i in range(n):
        price, taste = x[i]
        if price > d: break
        ans = max(ans, taste)
        rem = d - price
        ind = bs.less_than(rem + 1, prices).index
        if ind is not None:
            inde = bs.less_than(ind+1, cc).index
            if cc[inde] == i and inde == 0:continue
            if cc[inde] == i: inde-=1
            ans = max(ans, tastes[cc[inde]] + taste)
    print(ans)
