def C(n, m):
    res = []

    def rec(i):
        if len(res) == m:
            yield res.copy()
            return

        while i < n:
            res.append(i)
            for res_t in rec(i + 1):
                yield res_t
            i += 1
            res.pop()

    for res in rec(0):
        yield res


ans = list()
for e in C(3, 1):
    ans.append(e)
    print(e)
#print(len(ans))
