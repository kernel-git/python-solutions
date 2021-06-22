def A(n, m):
    kol = 1
    for i in range(m):
        kol *= n - i
    return kol


def get_nth(n, m, nth):
    mrk = [False] * n
    ans = []
    for i in range(m):
        a = A(n - i - 1, m - i - 1)
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


class Iterator:
    def __iter__(self):
        return self

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.count = 0
        self.maxn = A(n, m)

    def __next__(self):
        if self.count < self.maxn:
            self.count += 1
            return get_nth(self.n, self.m, self.count - 1)
        else:
            raise StopIteration


for gg in Iterator(4, 3):
    print(gg)
