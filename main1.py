import math


def gen(n, k):
    arr = [0] * n

    def rec(i, kk):
        if i == n:
            if kk == k:
                yield arr
            return
        if kk + 1 <= k:
            arr[i] = 1
            yield from rec(i + 1, kk + 1)
        arr[i] = 0
        yield from rec(i + 1, kk)

    yield from rec(0, 0)


def C(n, k):
    return int(math.factorial(n) / (math.factorial(n - k) * math.factorial(k)))


def get_nth(n, k, nth):
    ans = []
    kk = 0
    for i in range(0, n):
        c = C(n - i - 1, k - kk - 1)
        if nth <= c:
            ans.append(1)
            kk += 1
        else:
            nth -= c
            ans.append(0)

        if kk == k:
            break
    while len(ans) < n:
        ans.append(0)
    return ans


def gen2(n, k):
    for i in range(C(n, k)):
        yield get_nth(n, k, i + 1)


for gg in gen2(3, 1):
    print(gg)
