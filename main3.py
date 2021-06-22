import math


def gen(n):
    arr = [0] * n
    mrk = [False] * n

    def rec(i):
        if i == n:
            yield arr
            return
        for j in range(0, n):
            if mrk[j]:
                continue
            mrk[j] = True
            arr[i] = j + 1
            yield from rec(i + 1)
            mrk[j] = False

    yield from rec(0)


def get_nth(n, nth):
    mrk = [False] * n
    ans = []
    for i in range(n):
        a = math.factorial(n - i - 1)
        for j in range(n):
            if mrk[j]:
                continue
            if nth >= a:
                nth -= a
                continue
            ans.append(j + 1)
            mrk[j] = True
            break
    return ans


def gen2(n):
    for i in range(math.factorial(n)):
        yield get_nth(n, i)


for gg in gen2(4):
    print(gg)
