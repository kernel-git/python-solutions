# matrix = []
# n, m = int(input("n=")), int(input("m="))
# for i in range(n):
#     matrix.append([int(item) for item in input().split()])


def go(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return
    if matrix[x][y] == 0 or mrk[x][y]:
        return
    mrk[x][y] = True
    go(x + 1, y)
    go(x - 1, y)
    go(x, y + 1)
    go(x, y - 1)


n, m = 2, 3
matrix = [[1, 0, 1],
          [1, 1, 0]]
mrk = [[False for j in range(m)] for i in range(n)]

ans = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0 or mrk[i][j]:
            continue
        ans += 1
        go(i, j)

print(ans)
