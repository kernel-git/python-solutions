data = [[1,0,1,1,1],
        [0,0,0,0,0],
        [1,1,1,0,1],
        [0,1,0,0,1],
        [0,0,0,1,1]]


def fill(grid, n, m, i=0, j=0):
    if grid[i][j] == 0:
        return
    grid[i][j] = 0
    if i + 1 < m:
        fill(grid, n, m, i + 1, j)
    if j + 1 < n:
        fill(grid, n, m, i, j + 1)
    if i - 1 >= 0:
        fill(grid, n, m, i - 1, j)
    if j - 1 >= 0:
        fill(grid, n, m, i, j - 1)


def find_islands(grid, n, m, i=0, j=0):
    island = 0
    for k in range(n):
        for l in range(m):
            if grid[k][l] != 0:
                fill(grid, n, m, k, l)
                island += 1
    return island


print(find_islands(data, 5, 5))
