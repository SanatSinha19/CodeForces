T = int(input())
for _ in range(T):
    a, b, n = map(int, input().split())
    count = 0
    while max(a, b) <= n:
        if a < b:
            a += b
        else:
            b += a
        count += 1
    print(count)
