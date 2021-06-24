def A(n, m):
    res = []
    taken = set()

    def rec(i):
        if len(res) == m:
            yield res.copy()
            return

        while i < n:
            if i not in taken:
                res.append(i)
                taken.add(i)
                for res_t in rec(0):
                    yield res_t
                res.pop()
                taken.remove(i)
            i += 1

    for res in rec(0):
        yield res


ans = list()
for e in A(4, 2):
    ans.append(e)
    print(e)
print(len(ans))


