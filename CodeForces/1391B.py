t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    changes = 0
    for j in range(m - 1):
        if grid[n - 1][j] != 'R':
            changes += 1
    for i in range(n - 1):
        if grid[i][m - 1] != 'D':
            changes += 1
    print(changes)
